# reachable-stations
特定の地点から公共交通機関を用いて移動する際、**一定の所要時間・乗り換え回数の範囲内で到達可能な駅を列挙する**ためのツール。
到達可能な各駅について「名称」「緯度経度」「所要時間」「乗り換え回数」などを保持したGeoJSONを生成する。

指定地点からの到達可能駅の列挙にはNAVITIME Reachable APIを利用している。

## 使い方
### (1) RapidAPIの登録
NAVITIME Reachable APIをRapidAPI経由で利用することを想定しているため、[NAVITIME Reachable API - RapidAPI](https://rapidapi.com/navitimejapan-navitimejapan/api/navitime-reachable)でアカウントを作成する。

ブラウザのコンソール上でテストを行うことも可能だが、今回はヘッダの`x-rapidapi-key`で指定するAPIキーのみを利用し、レポジトリ内の`navitime.py`からリクエストを行う。

※ 一定以下のリクエスト数なら無料のBasicプランで利用可能。

### (2) 環境変数の設定
RapidAPIへの登録で得られたAPIキーを環境変数 `RAPIDAPI_KEY` にセットする。

```bash
export RAPIDAPI_KEY="YOUR_API_KEY"
```

### (3) 実行
以下の形式で実行する。ここで、`lat` / `lon` は始点とする地点の緯度経度を指定し、`geojson_name`には計算結果のファイル名（拡張子は`.geojson` / `.json`）を指定する。
```bash
python main.py lat lon geojson_name
```

例えば、(35.12345 138.12345) からの到達可能駅を`test.geojson`に保存したい場合、以下のようにする。
```bash
python main.py 35.12345 138.12345 test.geojson
```

## 条件の変更
以下の3つの条件は`navitime.py`の`NavitimeClient.search()`の引数で指定可能。`main.py`で勝手に値を指定しているので、必要に応じて修正する。
- `term_min` / `term_max`: 始点からの移動時間の上限・下限 (分)
    - `main.py`では0分〜60分としている
- `transit_limit`: 乗り換えの最大回数
    - `main.py`では1としているため、乗り換え0〜1回で到達可能な駅のみ列挙される

また、その他の（あまり変更する機会のなさそうな）条件は`navitime.py`で指定している。各項目の意味は公式ドキュメントを参照のこと。

## 利用例
所要時間で色分けし、路線図とともにWebマップ上に可視化

- https://github.com/sw1227/vue-reachability
- https://github.com/sw1227/tokyo-moving

## 参考
- [到達圏探索（トータルナビ） - NAVITIME API 2.0 仕様書](https://api-sdk.navitime.co.jp/api/specs/api_guide/reachable_transit.html)
- [NAVITIME Reachable API - RapidAPI](https://rapidapi.com/navitimejapan-navitimejapan/api/navitime-reachable)

