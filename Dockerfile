# Sử dụng hình ảnh Python chính thức
FROM python:3.10-slim

# Đặt thư mục làm việc trong container
WORKDIR /app

# Sao chép file requirements.txt vào container
COPY requirements.txt .

# Cài đặt các gói phụ thuộc
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép mã nguồn ứng dụng vào container
COPY . .

# Mở cổng 8000 (mặc định của Gunicorn)
EXPOSE 8000

# Lệnh mặc định để chạy ứng dụng Flask bằng Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
