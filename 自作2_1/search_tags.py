import sys
import csv

def search_tags(keyword, filename="danbooru.csv", max_results=30):
    keyword = keyword.lower()
    results = []

    try:
        # メモリを節約するため、ファイルを1行ずつ読み込む
        with open(filename, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            
            # ヘッダー行をスキップ（必要に応じて）
            header = next(reader, None)
            
            for row in reader:
                if not row:
                    continue
                
                # 行全体を小文字化してキーワードが含まれるかチェック
                row_str = ",".join(row).lower()
                
                if keyword in row_str:
                    # 通常、DanbooruのCSVは1列目(row[0])か2列目(row[1])にタグ名が入る
                    # ここでは確実に見せるため、行の最初の要素を取得
                    tag_name = row[0]
                    results.append(tag_name)
                    
                    # LLMのコンテキスト溢れを防ぐため、上限に達したら検索終了
                    if len(results) >= max_results:
                        break

    except FileNotFoundError:
        print(f"Error: '{filename}' が同じディレクトリに見つかりません。")
        sys.exit(1)
    except Exception as e:
        print(f"Error: ファイルの読み込み中にエラーが発生しました ({e})")
        sys.exit(1)

    return results

if __name__ == "__main__":
    # コマンドライン引数のチェック
    if len(sys.argv) < 2:
        print("Usage: python search_tags.py <keyword>")
        sys.exit(1)

    search_keyword = sys.argv[1]
    matches = search_tags(search_keyword)

    if matches:
        print(f"=== Results for '{search_keyword}' ===")
        for match in matches:
            print(match)
    else:
        print(f"No tags found matching '{search_keyword}'. Please try a different keyword.")