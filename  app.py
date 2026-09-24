import os
from flask import Flask

app = Flask(__name__)

# نستخدم رموز بديلة لتجنب مشاكل النسخ على الهاتف
Q = chr(34) * 3  # هذا الرمز يمثل """

# بناء صفحة HTML بطريقة آمنة
html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl" x-data="{ darkMode: localStorage.getItem('darkMode') === 'true' }" x-init="$watch('darkMode', val => localStorage.setItem('darkMode', val))" :class="{ 'dark': darkMode }">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ركن السعادة للتجارة | فرع الشحر</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: { extend: { colors: { brand: { pink: '#ec4899', dark: '#0b070d' } } } }
        }
    </script>
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;700;900&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Tajawal', sans-serif; transition: background-color 0.5s ease, color 0.5s ease; }
        .glass-card { background: rgba(255, 255, 255, 0.75); backdrop-filter: blur(14px); border: 1px solid rgba(236, 72, 153, 0.2); transition: all 0.3s ease; }
        .dark .glass-card { background: rgba(11, 7, 13, 0.75); border: 1px solid rgba(236, 72, 153, 0.15); }
        .pink-glow { text-shadow: 0 0 20px rgba(236, 72, 153, 0.6); }
        .dark .pink-glow { text-shadow: 0 0 25px rgba(236, 72, 153, 0.8); }
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-thumb { background: #ec4899; border-radius: 4px; }
        @keyframes fadeInUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
        .animate-fade-up { animation: fadeInUp 0.8s ease-out forwards; }
        @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-15px); } }
        .animate-float { animation: float 6s ease-in-out infinite; }
        @keyframes pulseSlow { 0%, 100% { opacity: 0.4; } 50% { opacity: 0.7; } }
        .animate-pulse-slow { animation: pulseSlow 4s cubic-bezier(0.4, 0, 0.6, 1) infinite; }
    </style>
</head>
<body class="bg-gray-50 text-gray-900 dark:bg-brand-dark dark:text-white overflow-x-hidden">

    <!-- Header -->
    <nav class="fixed top-0 w-full z-50 glass-card border-b border-pink-200 dark:border-pink-900/30 px-6 py-4 flex justify-between items-center shadow-sm">
        <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-full bg-gradient-to-tr from-brand-pink to-rose-400 flex items-center justify-center font-black text-xl text-white shadow-lg">س</div>
            <div>
                <span class="text-xl font-black block leading-none">ركن <span class="text-brand-pink">السعادة</span></span>
                <span class="text-[10px] text-gray-500 dark:text-pink-300 font-light tracking-widest">للتجارة - فرع الشحر</span>
            </div>
        </div>
        <div class="hidden md:flex gap-6 font-medium text-sm">
            <a href="#hero" class="hover:text-brand-pink transition-colors">الرئيسية</a>
            <a href="#about" class="hover:text-brand-pink transition-colors">من نحن</a>
            <a href="#products" class="hover:text-brand-pink transition-colors">الأقسام</a>
            <a href="#features" class="hover:text-brand-pink transition-colors">لماذا نحن</a>
            <a href="#contact" class="hover:text-brand-pink transition-colors">تواصل معنا</a>
        </div>
        <button @click="darkMode = !darkMode" class="p-2 rounded-full hover:bg-gray-200 dark:hover:bg-gray-800 transition-colors">
            <svg x-show="!darkMode" class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
            <svg x-show="darkMode" class="w-5 h-5 text-yellow-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
        </button>
    </nav>

    <!-- Hero -->
    <section id="hero" class="relative min-h-screen flex items-center justify-center pt-24 px-6 text-center overflow-hidden">
        <div class="absolute top-1/4 right-1/4 w-96 h-96 bg-brand-pink/20 rounded-full blur-3xl pointer-events-none animate-pulse-slow"></div>
        <div class="absolute bottom-1/4 left-1/4 w-96 h-96 bg-rose-500/15 rounded-full blur-3xl pointer-events-none animate-pulse-slow" style="animation-delay: 2s;"></div>
        <div class="max-w-4xl z-10 animate-fade-up">
            <span class="inline-block px-4 py-1.5 rounded-full glass-card text-brand-pink font-semibold text-xs mb-6 border border-pink-500/30">
                🛍️ أحدث تشكيلات الموضة والسجاد والمنسوجات في الشحر
            </span>
            <h1 class="text-4xl md:text-6xl font-black mb-6 leading-tight">
                عالم الأناقة والجمال في <br>
                <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-pink via-rose-400 to-amber-500 pink-glow">ركن السعادة للتجارة</span>
            </h1>
            <p class="text-gray-600 dark:text-gray-300 mb-8 max-w-2xl mx-auto font-light text-sm md:text-base">
                نقدم لكم أرقى الفساتين والملابس الجاهزة، وأجود أنواع السجاد والمنسوجات الفاخرة بأسعار مميزة وجودة عالية.
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="#products" class="bg-brand-pink hover:bg-pink-600 text-white font-bold px-8 py-3.5 rounded-xl shadow-xl transition-all hover:scale-105">تصفح الأقسام</a>
                <a href="https://wa.me/967780415415" target="_blank" class="glass-card hover:bg-gray-100 dark:hover:bg-white/10 font-bold px-8 py-3.5 rounded-xl transition-all hover:scale-105">📲 الطلب عبر الواتساب</a>
            </div>
        </div>
    </section>

    <!-- About -->
    <section id="about" class="py-20 px-6 max-w-7xl mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
            <div class="animate-fade-up">
                <span class="text-brand-pink font-bold text-sm mb-2 block">✨ قصتنا</span>
                <h2 class="text-3xl md:text-4xl font-black mb-6">من <span class="text-brand-pink">نحن</span>؟</h2>
                <p class="text-gray-600 dark:text-gray-300 leading-relaxed mb-4 text-sm md:text-base">
                    منذ انطلاقتنا في مدينة <strong>الشحر</strong> بمحافظة حضرموت، وضعنا نصب أعيننا هدفاً واحداً: أن نكون الوجهة الأولى لكل من يبحث عن الأناقة والجودة. في <strong>ركن السعادة للتجارة</strong>، نؤمن أن التفاصيل الصغيرة هي ما تصنع الفرق الكبير.
                </p>
                <p class="text-gray-600 dark:text-gray-300 leading-relaxed mb-6 text-sm md:text-base">
                    نحن لا نبيع مجرد ملابس أو سجاد، بل نقدم تجربة تسوق متكاملة تجمع بين الأصالة والحداثة.
                </p>
                <div class="flex gap-6">
                    <div><span class="block text-3xl font-black text-brand-pink">+10</span><span class="text-xs text-gray-500">سنوات خبرة</span></div>
                    <div><span class="block text-3xl font-black text-brand-pink">+5000</span><span class="text-xs text-gray-500">عميل سعيد</span></div>
                    <div><span class="block text-3xl font-black text-brand-pink">100%</span><span class="text-xs text-gray-500">جودة مضمونة</span></div>
                </div>
            </div>
            <div class="relative animate-fade-up" style="animation-delay: 0.2s;">
                <img src="https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&w=800&q=80" class="rounded-3xl shadow-2xl w-full h-96 object-cover border-4 border-white dark:border-gray-800">
                <div class="absolute -bottom-6 -right-6 w-32 h-32 bg-brand-pink rounded-full flex items-center justify-center text-white font-black text-xl shadow-xl animate-float">أصالة <br> وجودة</div>
            </div>
        </div>
    </section>

    <!-- Products -->
    <section id="products" class="py-16 px-6 max-w-7xl mx-auto bg-gray-100 dark:bg-white/5 rounded-3xl my-8">
        <div class="text-center mb-12 animate-fade-up">
            <h2 class="text-3xl font-black mb-2">أقسام <span class="text-brand-pink">المتجر</span></h2>
            <p class="text-gray-500 dark:text-gray-400 text-sm">تصفح أقسامنا المتنوعة واختر ما يناسبك</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <!-- 1 -->
            <div class="glass-card rounded-2xl overflow-hidden hover:border-brand-pink/50 transition-all duration-300 group animate-fade-up flex flex-row h-48">
                <div class="relative w-2/5 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                </div>
                <div class="p-4 w-3/5 flex flex-col justify-center">
                    <span class="text-brand-pink text-[10px] font-bold mb-1">ملابس نسائية</span>
                    <h3 class="text-base font-bold mb-1 group-hover:text-brand-pink transition-colors">فساتين وجلابيات</h3>
                    <p class="text-gray-500 dark:text-gray-400 text-[11px] mb-3 leading-relaxed">أرقى تصاميم الفساتين بتطريز أنيق.</p>
                    <a href="https://wa.me/967780415415" target="_blank" class="bg-brand-pink hover:bg-pink-600 text-white font-bold px-3 py-1.5 rounded-lg text-[11px] transition-all text-center">اطلب الآن</a>
                </div>
            </div>
            <!-- 2 -->
            <div class="glass-card rounded-2xl overflow-hidden hover:border-brand-pink/50 transition-all duration-300 group animate-fade-up flex flex-row h-48" style="animation-delay: 0.1s;">
                <div class="relative w-2/5 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1595777457583-95e059d581b8?auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                </div>
                <div class="p-4 w-3/5 flex flex-col justify-center">
                    <span class="text-brand-pink text-[10px] font-bold mb-1">عبايات</span>
                    <h3 class="text-base font-bold mb-1 group-hover:text-brand-pink transition-colors">عبايات وجلابيات</h3>
                    <p class="text-gray-500 dark:text-gray-400 text-[11px] mb-3 leading-relaxed">تصاميم عصرية وخامات مريحة.</p>
                    <a href="https://wa.me/967780415415" target="_blank" class="bg-brand-pink hover:bg-pink-600 text-white font-bold px-3 py-1.5 rounded-lg text-[11px] transition-all text-center">اطلب الآن</a>
                </div>
            </div>
            <!-- 3 -->
            <div class="glass-card rounded-2xl overflow-hidden hover:border-brand-pink/50 transition-all duration-300 group animate-fade-up flex flex-row h-48" style="animation-delay: 0.2s;">
                <div class="relative w-2/5 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1523381210434-271e8be1f52b?auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                </div>
                <div class="p-4 w-3/5 flex flex-col justify-center">
                    <span class="text-brand-pink text-[10px] font-bold mb-1">ملابس أطفال</span>
                    <h3 class="text-base font-bold mb-1 group-hover:text-brand-pink transition-colors">ملابس الأطفال</h3>
                    <p class="text-gray-500 dark:text-gray-400 text-[11px] mb-3 leading-relaxed">أزياء مريحة وعملية للأطفال.</p>
                    <a href="https://wa.me/967780415415" target="_blank" class="bg-brand-pink hover:bg-pink-600 text-white font-bold px-3 py-1.5 rounded-lg text-[11px] transition-all text-center">اطلب الآن</a>
                </div>
            </div>
            <!-- 4 -->
            <div class="glass-card rounded-2xl overflow-hidden hover:border-brand-pink/50 transition-all duration-300 group animate-fade-up flex flex-row h-48" style="animation-delay: 0.3s;">
                <div class="relative w-2/5 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1600121848594-d8644e57abab?auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                </div>
                <div class="p-4 w-3/5 flex flex-col justify-center">
                    <span class="text-brand-pink text-[10px] font-bold mb-1">سجاد ومفارش</span>
                    <h3 class="text-base font-bold mb-1 group-hover:text-brand-pink transition-colors">السجاد الفاخر</h3>
                    <p class="text-gray-500 dark:text-gray-400 text-[11px] mb-3 leading-relaxed">سجاد بجودة عالية ونقوش مميزة.</p>
                    <a href="https://wa.me/967780415415" target="_blank" class="bg-brand-pink hover:bg-pink-600 text-white font-bold px-3 py-1.5 rounded-lg text-[11px] transition-all text-center">اطلب الآن</a>
                </div>
            </div>
            <!-- 5 -->
            <div class="glass-card rounded-2xl overflow-hidden hover:border-brand-pink/50 transition-all duration-300 group animate-fade-up flex flex-row h-48" style="animation-delay: 0.4s;">
                <div class="relative w-2/5 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                </div>
                <div class="p-4 w-3/5 flex flex-col justify-center">
                    <span class="text-brand-pink text-[10px] font-bold mb-1">مفارش وستائر</span>
                    <h3 class="text-base font-bold mb-1 group-hover:text-brand-pink transition-colors">مفارش السرير</h3>
                    <p class="text-gray-500 dark:text-gray-400 text-[11px] mb-3 leading-relaxed">مجموعات متناسقة لتجديد منزلك.</p>
                    <a href="https://wa.me/967780415415" target="_blank" class="bg-brand-pink hover:bg-pink-600 text-white font-bold px-3 py-1.5 rounded-lg text-[11px] transition-all text-center">اطلب الآن</a>
                </div>
            </div>
            <!-- 6 -->
            <div class="glass-card rounded-2xl overflow-hidden hover:border-brand-pink/50 transition-all duration-300 group animate-fade-up flex flex-row h-48" style="animation-delay: 0.5s;">
                <div class="relative w-2/5 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                </div>
                <div class="p-4 w-3/5 flex flex-col justify-center">
                    <span class="text-brand-pink text-[10px] font-bold mb-1">منسوجات</span>
                    <h3 class="text-base font-bold mb-1 group-hover:text-brand-pink transition-colors">الأقمشة والمنسوجات</h3>
                    <p class="text-gray-500 dark:text-gray-400 text-[11px] mb-3 leading-relaxed">أجود أنواع الأقمشة والخامات.</p>
                    <a href="https://wa.me/967780415415" target="_blank" class="bg-brand-pink hover:bg-pink-600 text-white font-bold px-3 py-1.5 rounded-lg text-[11px] transition-all text-center">اطلب الآن</a>
                </div>
            </div>
            <!-- 7 -->
            <div class="glass-card rounded-2xl overflow-hidden hover:border-brand-pink/50 transition-all duration-300 group animate-fade-up flex flex-row h-48" style="animation-delay: 0.6s;">
                <div class="relative w-2/5 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                </div>
                <div class="p-4 w-3/5 flex flex-col justify-center">
                    <span class="text-brand-pink text-[10px] font-bold mb-1">عطور وبخور</span>
                    <h3 class="text-base font-bold mb-1 group-hover:text-brand-pink transition-colors">العطور والبخور</h3>
                    <p class="text-gray-500 dark:text-gray-400 text-[11px] mb-3 leading-relaxed">روائح فاخرة تدوم طويلاً.</p>
                    <a href="https://wa.me/967780415415" target="_blank" class="bg-brand-pink hover:bg-pink-600 text-white font-bold px-3 py-1.5 rounded-lg text-[11px] transition-all text-center">اطلب الآن</a>
                </div>
            </div>
            <!-- 8 -->
            <div class="glass-card rounded-2xl overflow-hidden hover:border-brand-pink/50 transition-all duration-300 group animate-fade-up flex flex-row h-48" style="animation-delay: 0.7s;">
                <div class="relative w-2/5 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1584917865442-de89df76afd3?auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                </div>
                <div class="p-4 w-3/5 flex flex-col justify-center">
                    <span class="text-brand-pink text-[10px] font-bold mb-1">حقائب وأحذية</span>
                    <h3 class="text-base font-bold mb-1 group-hover:text-brand-pink transition-colors">الحقائب والأحذية</h3>
                    <p class="text-gray-500 dark:text-gray-400 text-[11px] mb-3 leading-relaxed">تشكيلة أنيقة لتكتمل إطلالتك.</p>
                    <a href="https://wa.me/967780415415" target="_blank" class="bg-brand-pink hover:bg-pink-600 text-white font-bold px-3 py-1.5 rounded-lg text-[11px] transition-all text-center">اطلب الآن</a>
                </div>
            </div>
            <!-- 9 -->
            <div class="glass-card rounded-2xl overflow-hidden hover:border-brand-pink/50 transition-all duration-300 group animate-fade-up flex flex-row h-48" style="animation-delay: 0.8s;">
                <div class="relative w-2/5 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1606760227091-3dd870d97f1d?auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                </div>
                <div class="p-4 w-3/5 flex flex-col justify-center">
                    <span class="text-brand-pink text-[10px] font-bold mb-1">مستلزمات منزلية</span>
                    <h3 class="text-base font-bold mb-1 group-hover:text-brand-pink transition-colors">المستلزمات المنزلية</h3>
                    <p class="text-gray-500 dark:text-gray-400 text-[11px] mb-3 leading-relaxed">كل ما يحتاجه منزلك بجودة عالية.</p>
                    <a href="https://wa.me/967780415415" target="_blank" class="bg-brand-pink hover:bg-pink-600 text-white font-bold px-3 py-1.5 rounded-lg text-[11px] transition-all text-center">اطلب الآن</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Features -->
    <section id="features" class="py-20 px-6 max-w-7xl mx-auto">
        <div class="text-center mb-12 animate-fade-up">
            <h2 class="text-3xl font-black mb-2">لماذا تختار <span class="text-brand-pink">ركن السعادة</span>؟</h2>
            <p class="text-gray-500 dark:text-gray-400 text-sm">نحن نتميز بما نقدمه لعملائنا الكرام</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
            <div class="glass-card p-6 rounded-2xl text-center hover:-translate-