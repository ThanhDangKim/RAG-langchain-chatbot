# Chatbot Cung Cấp Thông Tin cho Trường Đại học Sư phạm Kỹ thuật

Dự án này nhằm xây dựng một chatbot thông minh có khả năng cung cấp thông tin chi tiết về trường Đại học Sư phạm Kỹ thuật. Chatbot được xây dựng bằng cách sử dụng các mô hình ngôn ngữ lớn (LLMs) và quy trình huấn luyện, tinh chỉnh để cải thiện độ chính xác và hiệu suất của mô hình. Dưới đây là hướng dẫn từng bước để triển khai dự án này.

## Mục Lục

1. [Giới Thiệu Đề Tài](#giới-thiệu)
2. [Mục Đích, Yêu Cầu Về Đề Tài ](#yêu-cầu)
3. [Các Bước Thực Hiện](#các-bước-thực-hiện)
    - [Bước 1: Chuẩn Bị Dữ Liệu](#bước-1-chuẩn-bị-dữ-liệu)
    - [Bước 2: Tinh Chỉnh Mô Hình Gốc](#bước-2-tinh-chỉnh-mô-hình-gốc)
    - [Bước 3: Truy Xuất Dữ Liệu Từ Database Vector](#bước-3-truy-xuất-dữ-liệu-từ-database-vector)
    - [Bước 4: Trả Lời Câu Hỏi](#bước-4-trả-lời-câu-hỏi)
4. [Cách Sử Dụng](#cách-sử-dụng)
5. [Kết Luận](#kết-luận)

## Giới Thiệu

Dự án này sử dụng các công nghệ hiện đại như ngôn ngữ lập trình Python và thư viện machine learning để xây dựng một chatbot có thể trả lời các câu hỏi liên quan đến trường Đại học Sư phạm Kỹ thuật. Dự án bao gồm các bước chuẩn bị dữ liệu, tinh chỉnh mô hình, truy xuất thông tin, và triển khai mô hình để trả lời câu hỏi.

## Yêu Cầu

Trước khi bắt đầu, hãy đảm bảo rằng bạn đã cài đặt các yêu cầu sau đây:

- Python 3.7+
- Các thư viện cần thiết: `nltk`, `numpy`, `pandas`, `transformers`, `sentence_transformers`, `langchain`, `pytorch`, `PyPDF2`, `pdfplumber`, `tqdm`, `re`, `pinecone`, `langchain_huggingface`, `langchain_community`, `accelerate`, `peft`, `bitsandbytes`, `trl`, `langchain_pinecone`

## Các Bước Thực Hiện

### Bước 1: Chuẩn Bị Dữ Liệu

Trước tiên, cần chuẩn bị dữ liệu đầu vào để huấn luyện mô hình chatbot. Chúng tôi sử dụng dữ liệu từ các tài liệu PDF, chuyển đổi chúng thành văn bản, và làm sạch dữ liệu để sử dụng trong huấn luyện.

- Mở file `prepare_data.ipynb` và chạy từng cell để:
  - Tải dữ liệu PDF từ thư viện trường.
  - Trích xuất văn bản và xử lý dữ liệu để loại bỏ các phần không cần thiết.
  - Lưu dữ liệu đã xử lý vào các tệp định dạng txt để sử dụng trong các bước sau.
  - Embedding các dữ liệu thành các vector và lưu lên cloud pinecone

### Bước 2: Tinh Chỉnh Mô Hình Gốc

Sau khi dữ liệu đã được chuẩn bị, chúng ta sẽ tinh chỉnh một mô hình ngôn ngữ lớn có sẵn (ví dụ: llama2, BERT, ...) bằng cách sử dụng dữ liệu đã xử lý.

- Mở file `finetune_model.ipynb` và chạy từng cell để:
  - Tải mô hình ngôn ngữ gốc từ thư viện `transformers`.
  - Huấn luyện mô hình trên tập dữ liệu đã chuẩn bị để mô hình học được các thông tin đặc thù của trường.
  - Lưu mô hình đã tinh chỉnh để sử dụng trong các bước tiếp theo.

### Bước 3: Truy Xuất Dữ Liệu Từ Database Vector

Sử dụng một cơ sở dữ liệu vector để lưu trữ và truy xuất thông tin một cách nhanh chóng và hiệu quả.

- Chạy file `vectorquery.py` để:
  - Tạo môi trường truy xuất cơ sở dữ liệu vector bằng cách sử dụng thư viện pinecone.
  - Gọi API để lấy được các dữ liệu liên quan đến prompts trên cloud.

### Bước 4: Trả Lời Câu Hỏi

Triển khai mô hình chatbot để trả lời câu hỏi từ người dùng.

- Chạy file `qabot.ipynb` để:
  - Tải mô hình đã tinh chỉnh và cơ sở dữ liệu vector.
  - Triển khai mô hình để trả lời các câu hỏi từ người dùng dựa trên truy vấn vector và kiến thức của mô hình.

## Cách Sử Dụng

1. **Chuẩn bị dữ liệu:** Chạy file `prepare_data.ipynb` để xử lý và chuẩn bị dữ liệu.
2. **Tinh chỉnh mô hình:** Chạy file `finetune_model.ipynb` để huấn luyện mô hình.
3. **Thiết lập cơ sở dữ liệu vector:** Chạy `vectorquery.py` để thiết lập cơ sở dữ liệu.
4. **Triển khai chatbot:** Chạy `qabot.ipynb` để bắt đầu trả lời câu hỏi từ người dùng.

## Kết Luận

Dự án chatbot này đã thành công trong việc xây dựng một hệ thống tự động trả lời câu hỏi về trường Đại học Sư phạm Kỹ thuật, tuy vẫn còn nhiều vấn đề chưa được xử lý như độ chính xác mô hình, thời gian phản hồi. Nhưng bằng cách sử dụng các công cụ và mô hình machine learning hiện đại, tôi đã có thể cải thiện đáng kể khả năng truy vấn và trả lời câu hỏi, tạo ra một công cụ hữu ích cho sinh viên và người quan tâm đến thông tin về trường.

---

## Contact me

- dangkimthanh281003@gmail.com
