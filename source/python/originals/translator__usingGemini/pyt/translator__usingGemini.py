#!/usr/bin/env python3
import os, sys, re
import google.generativeai as genai
import nkTextProcess.extract__textFromPDF as etp
import nkTextProcess.convert__text2pdf    as t2p

# ========================================================= #
# ===  translator__usingGemini.py                       === #
# ========================================================= #

def translator__usingGemini( text_en=None, input_pdfFile=None, output_pdfFile=None, \
                             input_txtFile=None, \
                             english_txtFile=None, japanese_txtFile=None, chunksize=800, \
                             fontsize=9.0, silent=True ):

    # ------------------------------------------------- #
    # --- [1] load text from pdf                    --- #
    # ------------------------------------------------- #
    if ( input_pdfFile is not None ):
        if ( output_pdfFile is     None ):
            output_pdfFile = input_pdfFile.replace( ".pdf", "_ja.pdf" )
        text_en  = etp.extract__textFromPDF( inpFile=input_pdfFile, outFile=english_txtFile, \
                                             remove_return=True )
        
    # ------------------------------------------------- #
    # --- [2] load text from text file              --- #
    # ------------------------------------------------- #
    if ( input_txtFile is not None ):
        # -- read file -- #
        with open( input_txtFile, "r" ) as f:
            text  = f.read()
        text      = " ".join( text.split() )
        sentences = re.split( r"(?<=[.!?])\s+", text )
        
        # -- chunking -- #
        text_en, stack = [], []
        count          =  0
        for sentence in sentences:
            stack += [ sentence ]
            count += len( sentence.split() )
            if ( ( count > chunksize ) and ( count > 0 ) ):
                text_en += [ " ".join( stack ) ]
                stack    = []
                count    = 0
        if ( len( stack ) > 0 ):
            text_en += [ " ".join( stack ) ]

        # -- output pdf name -- #
        if ( output_pdfFile is None ):
            base_name, extension = os.path.splitext( input_txtFile )
            output_pdfFile       = base_name + "_ja.pdf"

    if ( text_en is None ):
        sys.exit( " text_en == ???, input_pdf / input_txt must be given" )
            
    # ------------------------------------------------- #
    # --- [3] prepare gemini                        --- #
    # ------------------------------------------------- #
    #  -- Gemini APIの設定                          --  #
    #  -- export GEMINI_API_KEY="api key"           --  #
    my_api_key = os.environ.get( "GEMINI_API_KEY" )
    genai.configure( api_key=my_api_key )
    # model      = genai.GenerativeModel('gemini-pro')
    model      = genai.GenerativeModel()
    # prompt     = f"以下の英語論文の文章を日本語訳してください．pdfから抜き出した文字列のため、ページ番号や図のキャプションが途中に混じっている場合があります．それらは、適宜、無視するなどし、本文として一連の意味が通じるように翻訳してください．：\n\n{stack_en}"

    # ------------------------------------------------- #
    # --- [4] translator into japanese              --- #
    # ------------------------------------------------- #
    text_stack = []
    print( len( text_en ) )
    for ik,piece in enumerate( text_en ):
        prompt     = f"以下の英語論文の文章を日本語訳してください．pdfから抜き出した文字列のため、ページ番号や図のキャプションが途中に混じっている場合があります．それらは、適宜、無視するなどし、本文として一連の意味が通じるように翻訳してください．：\n\n{piece}"
        response    = model.generate_content( prompt )
        piece_ja    = response.text
        text_stack += [ piece_ja ]
    text_ja = " ".join( text_stack )
    
    # ------------------------------------------------- #
    # --- [5] save in a file                        --- #
    # ------------------------------------------------- #
    if ( not( silent ) ):
        print( "\n" + "-"*70 +"\n"  )
        print( text_ja )
        print( "\n" + "-"*70 +"\n"  )
        
    if ( japanese_txtFile is not None ):
        with open( japanese_txtFile, "w" ) as f:
            f.write( text_ja )

    # ------------------------------------------------- #
    # --- [5] convert into japanese pdf             --- #
    # ------------------------------------------------- #
    t2p.convert__text2pdf( outFile=output_pdfFile, texts=text_stack, fontsize=fontsize )
    
    # ------------------------------------------------- #
    # --- [6] return                                --- #
    # ------------------------------------------------- #
    return( text_ja )


# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):

    # ------------------------------------------------- #
    # --- [1] arguments                             --- #
    # ------------------------------------------------- #
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument( "--input_pdf"     , default=None, help="input pdf file"     )
    parser.add_argument( "--input_txt"     , default=None, help="input text file"    )
    parser.add_argument( "--output_pdf"    , default=None, help="output pdf file"    )
    parser.add_argument( "--chunksize"     , default= 800, help="text chunk size"    )
    parser.add_argument( "--english_text"  , default=None, help="english_text_file"  )
    parser.add_argument( "--japanese_text" , default=None, help="japanese_text_file" )
    parser.add_argument( "--fontsize"      , type=float, default=9.0, help="font size"        )
    parser.add_argument( "--show"          , type=bool , default=False, help="display or not" )
    parser.add_argument( "--intermediate"  , type=bool , default=False, help="intermidiate file out" )
    
    args   = parser.parse_args()

    if   ( args.input_pdf ):
        input_file = str( args.input_pdf )
    elif ( args.input_txt ):
        input_file = str( args.input_txt )
    else:
        print( "[ How to use ] python translator__usingGemini.py --input_pdf xxx.pdf " )
        sys.exit()
        
    if ( args.intermediate ):
        if ( args.english_text  is None ): args.english_text  = "text_en.txt"
        if ( args.japanese_text is None ): args.japanese_text = "text_ja.txt"

    # ------------------------------------------------- #
    # --- [2] call translator                       --- #
    # ------------------------------------------------- #
    print( "[translator__usingGemini.py] translation of {}".format( input_file ) )
    translator__usingGemini( input_pdfFile=args.input_pdf, output_pdfFile=args.output_pdf, \
                             input_txtFile=args.input_txt, chunksize=args.chunksize, \
                             english_txtFile=args.english_text, \
                             japanese_txtFile=args.japanese_text,\
                             fontsize=args.fontsize, silent=not( args.show ) )



