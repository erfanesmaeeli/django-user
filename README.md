# django-user
Extend Django User Model
<br>
A Full Account App

<br>
<div dir="rtl">
  <h3>
  اولین قدم برای شروع یک پروژه، پیاده‌سازی زیرساخت اپلیکیشن یوزر هست.
  </h3>

<blockquote>
  در این پروژه سعی کردم یک اپلیکیشن کامل برای کاربر ایجاد کنم که حداقلیات را داشته باشد و بتوانیم با خیال راحت داخل پروژه‌هامون استفاده کنیم و اگر نیاز به موارد بیشتر هست میتوانیم بعدا به آن اضافه کنیم
</blockquote>
  </div>
<hr>
<br>
<div dir="rtl">
در این اپلیکیشن تمامی تاریخ‌ها به شمسی تغییر پیدا کرده است. پس لازمه پکیج django-jalali را نصب کنید:
</div>
<br>
<div class="highlight highlight-source-shell">
  <pre>$ pip install django-jalali</pre>
</div>

<br>
<div dir="rtl">
 سپس آنرا به INSTALLED_APPS اضافه کنید.
  <small>(بهتر است آنرا قبل از سایر اپلیکیشن‌ها تعریف کنید.)</small>
</div>
<br>
<div class="highlight highlight-source-shell">
  <pre>'django_jalali',</pre>
</div>

<br>


<div dir="rtl">
در آخر با دستور زیر جداول مایگیریشن را در دیتابیس ایجاد میکنیم:
</div>
<br>
<div class="highlight highlight-source-shell">
  <pre>$ python manage.py migrate
</pre>
</div>

<br>
