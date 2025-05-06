import os, sys, re, glob, json5, tqdm
import extract_msg
import datetime
import google.generativeai as genai

# ========================================================= #
# ===  gemini__summary                                  === #
# ========================================================= #
def gemini__summary( path="msg/*.msg", outFile="dat/output.json", \
                     html_config="dat/html_config.json" ):

    # ------------------------------------------------- #
    # --- [1] search filename                       --- #
    # ------------------------------------------------- #
    filenames = glob.glob( path.lower() )
    stack     = {}

    # ------------------------------------------------- #
    # --- [2] summarize content                     --- #
    # ------------------------------------------------- #
    for ik, filename in enumerate( tqdm.tqdm( filenames, desc="Processing files" ) ):
        IDno     = "{:06}".format(ik+1)
        msg      = extract_msg.Message( filename )
        date     = ( msg.date ).strftime( '%Y/%m/%d' )
        subject  = msg.subject
        body     = msg.body
        prompt   = f"以下の転送メールについて、メール冒頭の「転送者の私見」とそれに続く「記事」を分けてください．私見は、[opinion]、記事は[content]のタグをつけて抜き出してください．私見は、冒頭の宛名や末尾の送信者の名前や署名、「お世話になります」などの挨拶が含まれる場合は取り除いて内容のみにしてください．また、記事は日本語３行で要約し、[summary]のタグをつけてください．３行の要約は、 '* ' から開始し、１行毎に改行してください．また、記事に放射性核種(At-211やAc225, 226Ra、単にCupperや銅、など)が言及される場合、放射性核種を[nuclide]のタグをつけて抜き出し・列挙してください．また、記事に会社名が含まれる場合、会社名を[company]のタグをつけて抜き出し・列挙してください．ただし、日立ハイテクや日立は除外してください．タグの記載順は、[opinion], [content], [summary], [nuclide], [company] の順としてください．：\n\n{body}"
        response = model.generate_content( prompt )
        texts    = response.text
        pattern1 = "\[opinion\](.*)\[content\]"
        pattern2 = "\[content\](.*)\[summary\]"
        pattern3 = "\[summary\](.*)\[nuclide\]"
        pattern4 = "\[nuclide\](.*)\[company\]"
        pattern5 = "\[company\](.*)"
        opinion  = ( ( re.search( pattern1, texts, flags=re.DOTALL ) ).group(1) ).strip()
        content  = ( ( re.search( pattern2, texts, flags=re.DOTALL ) ).group(1) ).strip()
        summary  = ( ( re.search( pattern3, texts, flags=re.DOTALL ) ).group(1) ).strip()
        nuclide  = ( ( re.search( pattern4, texts, flags=re.DOTALL ) ).group(1) ).strip()
        company  = ( ( re.search( pattern5, texts, flags=re.DOTALL ) ).group(1) ).strip()
        info     = { "No.":IDno, "filename":filename, "date":date, "subject":subject, \
                     "opinion":opinion, "content":content, "summary":summary, \
                     "nuclide":nuclide, "company":company }
        stack[ IDno ] = info

    # ------------------------------------------------- #
    # --- [3] sort and renumber                     --- #
    # ------------------------------------------------- #
    sorted_items = sorted( stack.items(), key=lambda x: datetime.datetime.strptime( x[1]['date'], '%Y/%m/%d') )
    stack_       = {}
    for ik, ( _, item ) in enumerate( sorted_items, 1 ):
        IDno            = "{:06}".format( ik )
        item["No."]     = IDno
        stack_[ IDno  ] = item
    stack = stack_
        
    # ------------------------------------------------- #
    # --- [4] save as json file                     --- #
    # ------------------------------------------------- #
    with open( outFile, "w" ) as f:
        json5.dump( stack, f, ensure_ascii=False )
    return( stack )
        
        
# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument( "--msgPath"      , help="path to the .msg ( msg/*.msg etc. )", \
                         default="msg/*.msg" )                ## optional
    parser.add_argument( "--outFile"      , help="output file name.", \
                         default="dat/output.json" )          ## optional
    parser.add_argument( "--html_config"  , help="output file name.", \
                         default="dat/output.json" )          ## optional
    parser.add_argument( "-n", "--no_gemini", help="no gemini api",\
                         default=False, action="store_true" ) ## flag
    args   = parser.parse_args()
    no_gemini = args.no_gemini
    msgPath   = args.msgPath
    outFile   = args.outFile
    
    # ------------------------------------------------- #
    # --- [1] gemini configuration                  --- #
    # ------------------------------------------------- #
    # Gemini APIの設定
    # export GEMINI_API_KEY="api key"
    my_api_key = os.environ.get( "GEMINI_API_KEY" )
    genai.configure( api_key=my_api_key )
    model      = genai.GenerativeModel()

    # ------------------------------------------------- #
    # --- [2] gemini summarizing                    --- #
    # ------------------------------------------------- #
    if ( not( no_gemini ) ):
        gemini__summary( msgPath, outFile=outFile )
    
    # ------------------------------------------------- #
    # --- [3] summarize as a html page              --- #
    # ------------------------------------------------- #
    import nkUtilities.generate__html as htm
    htm.generate__html( html_config=html_config, silent=True )
