# Textura WEB

### Инструмент комплексного анализа текста по относительным числовым показателям

Textura – DH-приложение для анализа свойств текста в сравнении с текстами НКРЯ по числовым показателям.  

Проект нацелен на помощь цифровым гуманитарным исследователям, литературоведам и другим пользователям, работающим с отдельно взятыми текстами. 

Мы верим в потенциал анализа текста по количественным метрикам в сравнении с большим корпусом для современных гуманитарных исследований. 

Более полное описание TEXTURA доступно в [официальной статье](https://docs.google.com/document/d/1gi-7A69SDtH7Pp8TjVJWitFL3kkwZhgcatr2nBVNuz4/edit#heading=h.b92faztiq4z2), посвященной проекту. 

Над проектом работали:
- Николай Горбачев
- Татьяна Чечельницкая
- Александр Симанычев

## Установка

### Mac/Linux

1. Загрузить .ZIP архив: **Code** -> **Download ZIP**

2. Перейти в загруженную папку в терминале:

`cd .../<Downloads Folder>/textura-main`

3. Ввести в терминале:

`sh mac-install.sh`

`sh mac-run.sh`

### Windows

1. Загрузить .ZIP архив: **Code** -> **Download ZIP**

2. Перейти в загруженную папку в командной строке:

`cd .../<Downloads Folder>/textura-main`

3. Скопировать и вставить в командной строке:

`python -m pip install --upgrade pip && python -m pip install --user virtualenv && python -m venv textura_env && .\textura_env\Scripts\activate && pip install -r requirements.txt && deactivate`

`.\textura_env\Scripts\activate && python run.py && deactivate`

## Использование

1. Загрузка текста: загрузить текст во вкладке *Загрузить текст* в формате .txt
2. Анализ: нажмите зеленую кнопку *Анализировать текст* на первой вкладке -- Textura обработает текст и вернет анализ по количественным метрикам.
3. Графики сравнения с корпусом: на странице анализа по нажатию зеленой кнопки отрисуются графики для сравнения вашего текста с текстами НКРЯ по всем метрикам
4. Фильтрация корпуса: кнопка фильтрации на странице анализа позволяет выбрать подгруппу текстов для сравнения с этой подгруппой вашего загруженного текста
5. Интерпретация: на основе полученных результатов вы можете получить представление о характеристиках текста. Например, если инструмент показывает высокий уровень индексов удобочитаемости языка, вы можете сделать вывод о сложности текста относительно других текстов.
6. Проверьте другие тексты: если вы хотите проанализировать другой текст, вернитесь на главную страницу или нажмите кнопку «Загрузить текст»

## Список метрик

Список метрик в группировке по гуманитарным свойствам, за которые они отвечают:

1. Базовые метрики
    - Среднее арифметическое длины предложений в тексте
    - Медиана длины предложений в текста
    - Среднее арифметическое длины слов в тексте
    - Медиана длины слов в текста
    - Среднее количество слогов в словах
2. Лексика текста
    - Коэффициент лексического разнообразия (lexical diversity) -- количественная характеристика текста, отражающая степень богатства словаря при построении текста заданной длины. В основе показателя лежит соотношение числа отдельных лексических единиц (лемм, англ. types) и количества их употреблений в тексте (текстоформ, англ. tokens). Вычисляется как отношение количества лемм к количеству текстоформ (токенов)
    - Коэффициент лексической плотности (lexical density) -- отношение самостоятельных частей речи в тексте к общему количеству слов. Более лексически плотными, таким образом, будут тексты, в которых используется меньше служебной лексики.
3. Сложность текста для восприятия
    - Количетсво многосложных слов (более чем два слога)
    - Индекс удобочитаемости -- Автоматический индекс удобочитаемости (англ. automated readability index (ARI)) — мера определения сложности восприятия текста читателем, аппроксимирующая сложность текста к номеру класса в американской системе образования, ученикам которого данный текст будет понятен.
    - FRES -- одна из формул определения индекса удобочитаемости, учитывающая среднее количество слогов
    - Gunning fog index -- одна из формул определения индекса удобочитаемости, учитывающая количество многосложных слов
    - SMOG -- одна из формул определения индекса удобочитаемости, зависящая от количества предложений
    - CLI -- одна из формул определения индекса удобочитаемости, зависящая от средней длины предложений и средней длины слов
4. Анализ тональности
Анализ тональности приведен в тестовом режиме и работает через модель DeepPavlov/rubert-base-cased-conversational обученной на RuSentiment.
    - blanchefort_positive -- средняя позитивная оценка по предложениям в тексте
    - blanchefort_neutral -- средняя нейтральная оценка по предложениям в тексте
    - blanchefort_negative -- средняя негативная оценка по предложениям в тексте
