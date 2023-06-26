# Ví dụ mã này trình bày cách đọc mã QR không chính xác trong Python.
import aspose.barcode as barcode

# Tải hình ảnh mã QR
reader = barcode.barcoderecognition.BarCodeReader(r"D:\student-ID-PTIT-OCR\356255331_3309990212551698_4262570826321098954_n.jpg")

# Chỉ định cài đặt chất lượng để đọc mã QR nhỏ và không chính xác
reader.quality_settings.read_tiny_barcodes = True
reader.quality_settings.allow_incorrect_barcodes = True

# Đọc mã QR
recognized_results = reader.read_bar_codes()

# Hiển thị kết quả
for x in recognized_results:
    print("Code Text: " + x.code_text)
    print("Type: " + x.code_type_name)
