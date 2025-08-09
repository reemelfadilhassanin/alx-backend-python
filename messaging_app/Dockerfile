# استخدم صورة Python 3.10 الرسمية كأساس
FROM python:3.10-slim

# تحديد مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ ملف المتطلبات إلى داخل الحاوية
COPY requirements.txt .

# تثبيت المكتبات
RUN pip install --no-cache-dir -r requirements.txt

# نسخ جميع ملفات المشروع إلى داخل الحاوية
COPY . .

# كشف البورت 8000 (بورت الدجانجو الافتراضي)
EXPOSE 8000

# الأمر لتشغيل التطبيق (يتم تعديل هذا حسب كيفية تشغيلك للتطبيق)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
