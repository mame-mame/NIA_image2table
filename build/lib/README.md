# table_ocr_to_png
***
*원본 소스: <https://github.com/eihli/image-table-ocr>

*실행 코드: mame-mame/table_ocr/__image2table__.py

*경로 수정 방법: mame-mame/table_ocr/__image2table__.py 내에 file_dir에 이미지파일들(png)이 있는 폴더 경로 지정, save_dir에 저장될 폴더 경로 지정(없을시 자동 생성)
***

##__main__.py를 통한 현재 구현 기능

1. 이미지 파일(.png)에서 표(테이블)이 있는 이미지 파일에서 표만 추출하여 폴더 생성 후 이미지 파일(.png)로 저장

2. 표 이미지 파일(.png)에서 전처리 후 각 셀을 추출, 폴더 생성 후 이미지 파일(.png)로 저장

3. 셀 이미지 파일을 OCR하기 편하게 전처리 작업 후 폴더 생성 이미지 파일로 저장

4. 전처리 된 셀 이미지 파일(.png)을 OCR 작업을 거친 후 각 셀 이미지 파일(.png)에 대한 텍스트 파일(.gt.txt) 생성 및 전체 csv 파일, html 파일 생성

5. 터미널에 html table 코드 출력



## 추후 추가/ 변경 예정 사항
1. OCR라이브러리 변경(Tesseract -> EasyOCR)
