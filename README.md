# Семинар 1

## Домашнее задание

## 1. Задание 1

В классе Calculator создайте метод calculateDiscount, который принимает сумму покупки и процент скидки и возвращает сумму с учетом скидки.
Ваша задача - проверить этот метод с использованием библиотеки AssertJ.

Если метод calculateDiscount получает недопустимые аргументы, он должен выбрасывать исключение ArithmeticException.
Не забудьте написать тесты для проверки этого поведения.

## 2. Задание 2

Мы хотим улучшить функциональность нашего интернет-магазина. Ваша задача - добавить два новых метода в класс Shop:
Метод sortProductsByPrice(), который сортирует список продуктов по стоимости.
Метод getMostExpensiveProduct(), который возвращает самый дорогой продукт.

Напишите тесты, чтобы проверить, что магазин хранит верный список продуктов (правильное количество продуктов, верное содержимое корзины).
Напишите тесты для проверки корректности работы метода getMostExpensiveProduct. Напишите тесты для проверки корректности работы метода sortProductsByPrice (проверьте правильность сортировки). Используйте класс Product для создания экземпляров продуктов и класс Shop для написания методов сортировки и тестов.

# Семинар 2

## Обзор кода проекта

Проект представляет собой простую модель онлайн-магазина, в котором имеются следующие основные компоненты:
1. Product: Класс, представляющий продукт. У каждого продукта есть идентификатор, название, цена и
количество.
2. Shop: Класс, представляющий магазин. У каждого магазина есть список продуктов, которые он предлагает.
3. Cart: Класс, представляющий корзину покупателя. В корзину можно добавлять и удалять товары, а также
рассчитывать общую стоимость товаров в корзине.
4. TextUserInterface: Класс, представляющий текстовый пользовательский интерфейс, который предлагает
пользователю варианты действий, такие как просмотр продуктов магазина, добавление и удаление товаров из
корзины.

Важными методами являются addProductToCartByID и removeProductByID, которые добавляют и удаляют продукт из
корзины соответственно. Вся логика по обновлению количества товаров в магазине и корзине, а также пересчете
общей стоимости товаров, инкапсулирована в этих методах.

## Задания
1. Разработайте модульный тест для проверки, что общая стоимость корзины с разными товарами корректно рассчитывается
2. Создайте модульный тест для проверки, что общая стоимость корзины с множественными экземплярами одного и того же продукта корректно рассчитывается.
3. Напишите модульный тест для проверки, что при удалении товара из
корзины происходит перерасчет общей стоимости корзины.
4. Разработайте модульный тест для проверки, что при добавлении определенного количества товара в корзину, общее количество этого товара в магазине соответствующим образом уменьшается.
5. Создайте модульный тест для проверки, что если пользователь забирает все имеющиеся продукты определенного типа из магазина, эти продукты больше не доступны для заказа.
6. Напишите модульный тест для проверки, что при удалении товара из корзины, общее количество этого товара в магазине соответствующим образом увеличивается.
7. Разработайте параметризованный модульный тест для проверки, что при вводе неверного идентификатора товара генерируется исключение RuntimeException.
8. Создайте модульный тест для проверки, что при попытке удалить из корзины больше товаров, чем там есть, генерируется исключение RuntimeException.

## Домашнее задание

## Обзор кода проекта
### Vehicle
В этом проекте, вы будете работать с проектом "Vehicle", который представляет собой иерархию классов, включающую абстрактный базовый класс "Vehicle" и два его подкласса "Car" и "Motorcycle".

Базовый класс "Vehicle" содержит абстрактные методы "testDrive()" и "park()", а также поля "company", "model", "yearRelease", "numWheels" и "speed".

Класс "Car" расширяет "Vehicle" и реализует его абстрактные методы. При создании объекта "Car", число колес устанавливается в 4, а скорость в 0. В методе "testDrive()" скорость устанавливается на 60, а в методе "park()" - обратно в 0.

Класс "Motorcycle" также расширяет "Vehicle" и реализует его абстрактные методы. При создании объекта "Motorcycle", число колес устанавливается в 2, а скорость в 0. В методе "testDrive()" скорость устанавливается на 75, а в методе "park()" - обратно в 0.

## Задания
Проект Vehicle. Написать следующие тесты с использованием JUnit5:
- Проверить, что экземпляр объекта Car также является экземпляром транспортного средства (используя
оператор instanceof).
- Проверить, что объект Car создается с 4-мя колесами.
- Проверить, что объект Motorcycle создается с 2-мя колесами.
- Проверить, что объект Car развивает скорость 60 в режиме тестового вождения (используя метод testDrive()).
- Проверить, что объект Motorcycle развивает скорость 75 в режиме тестового вождения (используя метод testDrive()).
- Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта) машина останавливается (speed = 0).
- Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта) мотоцикл останавливается (speed = 0).

# Семинар 3

## Задание №1
Создайте набор тестов, полностью покрывающих все ветви кода функции fizzBuzz. Эта функция принимает на вход число и возвращает "Fizz", если число делится на 3, "Buzz", если число делится на 5, и "FizzBuzz", если число делится на 15. Если число не делится ни на 3, ни на 5, ни на 15, функция возвращает входное число в виде строки.

## Задание №2
Разработайте тесты для метода firstLast6, где на вход подается массив чисел, а метод возвращает true, если первое или последнее число в массиве равно 6, иначе false.

## Задание №3
Создайте тесты, обеспечивающие полное покрытие кода метода calculatingDiscount, который принимает сумму покупки и размер скидки, затем вычисляет и возвращает сумму с учетом скидки. Метод должен обрабатывать исключения, связанные с некорректным размером скидки или отрицательной суммой покупки.

## Задание №4
Разработайте метод luckySum и напишите для него тесты. Этот метод принимает на вход три числа и возвращает их сумму. Однако, если одно из чисел равно 13, то оно не учитывается при подсчете суммы.

Так, например, если b равно 13, то считается сумма только a и c.

## Задание №5
Примените подход TDD для создания нового класса MoodAnalyser, который оценивает настроение выраженное во фразах.

## Задание №6
Разработайте класс User с методом аутентификации по логину и паролю. Метод должен возвращать true, если введенные логин и пароль корректны, иначе false. Протестируйте все методы

## Задание №7
Добавьте класс UserRepository для управления пользователями. В этот класс должен быть включен метод addUser, который добавляет пользователя в систему, если он прошел аутентификацию. Покройте тестами новую функциональность

# Домашнее задание
## Задание 1
Напишите тесты, покрывающие на 100% метод evenOddNumber, который проверяет, является ли переданное число четным или нечетным

## Задание 2
Разработайте и протестируйте метод numberInInterval, который проверяет, попадает ли переданное число в интервал (25;100)

## Задание 3.*
Добавьте функцию в класс UserRepository, которая разлогинивает всех пользователей, кроме администраторов. Для этого, вам потребуется расширить класс User новым свойством, указывающим, обладает ли пользователь админскими правами. Протестируйте данную функцию.

# Семинар 4

## Задание №1
Создать мок-объект Iterator, настроить поведение так, чтобы за два вызова next() Iterator вернул два слова “Hello World”, и проверить это поведение с помощью утверждений

## Задание №2
Используя библиотеку Mockito, напишите модульные тесты для проверки функциональности формы оплаты на сайте. Вместо реальной кредитной карты используйте мок-объект.
1. Создайте класс `CreditCard` с методами `getCardNumber()`, `getCardHolder()`, getExpiryDate()`, `getCvv()`, `charge(double amount)`.
2. Создайте класс `PaymentForm` с методом `pay(double amount)`.
3. В тестовом классе, создайте мок-объект для класса `CreditCard`.
4. Определите поведение мок-объекта с помощью метода `when()`.
5. Создайте объект класса `PaymentForm`, передайте ему мок-объект в качестве аргумента.
6. Вызовите метод `pay()` и убедитесь, что мок-объект вызывает метод `charge()`.

## Задание №3
Предположим, у вас есть класс WeatherService, который имеет метод getCurrentTemperature(), обращающийся к внешнему API для получения информации о текущей температуре.

Вам нужно протестировать другой класс, WeatherReporter, который использует WeatherService. Создайте мок-объект для WeatherService с использованием Mockito.

## Задание №4
Вам необходимо написать тест с использованием моков для сервиса бронирования отелей.

Условие: У вас есть класс HotelService с методом public boolean isRoomAvailable(int roomId), который обычно проверяет, доступен ли номер в отеле.

Вам необходимо проверить правильность работы класса BookingService, который использует HotelService для бронирования номера, если он доступен.

## Задание №5
Вам нужно написать тест с использованием моков для сервиса отправки сообщений.

Условие: У вас есть класс MessageService с методом public void sendMessage(String message, String recipient), который отправляет сообщение получателю.

Вам необходимо проверить правильность работы класса NotificationService, который использует MessageService для отправки уведомлений.

## Задание №6
Вам требуется протестировать класс, который обрабатывает запросы к базе данных.

Условие: У вас есть класс Database с методом public List<String> query(String sql), который выполняет SQLзапрос и возвращает результат.

Вам необходимо проверить правильность работы класса DataProcessor, который использует Database для
выполнения запроса и обработки результатов.

## Задание №7
Вам нужно написать тест с использованием моков для класса, который выполняет HTTP-запросы.

Условие: У вас есть класс HttpClient с методом public String get(String url), который выполняет HTTP-запрос и возвращает результат.

Вам необходимо проверить правильность работы класса WebService, который использует HttpClient для получения данных с веб-сайта.

## Домашнее задание

## Задание 1.
### Ответьте письменно на вопросы:
1. Почему использование тестовых заглушек может быть полезным при написании модульных тестов?
2. Какой тип тестовой заглушки следует использовать, если вам нужно проверить, что метод был вызван с определенными аргументами?
3. Какой тип тестовой заглушки следует использовать, если вам просто нужно вернуть определенное значение или исключение в ответ на вызов метода?
4. Какой тип тестовой заглушки вы бы использовали для имитации взаимодействия с внешним API или базой данных?

## Задание 2.
У вас есть класс BookService, который использует интерфейс BookRepository для получения информации о книгах из базы данных.

Ваша задача написать unit-тесты для BookService, используя Mockito для создания мок-объекта BookRepository.

# Семинар 5

## Задание №1
Создайте два модуля. Первый модуль генерирует список случайных чисел. Второй модуль находит максимальное число в этом списке. 

Вам нужно сначала написать юнит-тесты для каждого модуля, затем написать интеграционный тест, который проверяет, что оба модуля работают вместе правильно.

## Задание №2
У вас есть два класса - UserService и UserRepository. UserService использует UserRepository для получения информации о пользователе.

Ваша задача - написать интеграционный тест, который проверяет, что UserService и UserRepository работают вместе должным образом.

## Задание №3
У вас есть сервис по обработке заказов, состоящий из двух классов: OrderService и PaymentService.

Класс OrderService обрабатывает заказы и делает вызовы к PaymentService для обработки платежей.

Ваша задача - написать интеграционный тест, который проверяет, что OrderService и PaymentService взаимодействуют корректно

## Задание №4
Напишите автоматизированный тест, который выполнит следующие шаги:
1. Открывает главную страницу Google.
2. Вводит "Selenium" в поисковую строку и нажимает кнопку "Поиск в Google".
3. В результатах поиска ищет ссылку на официальный сайт Selenium (https://www.selenium.dev) и проверяет, что ссылка действительно присутствует среди результатов поиска.

## Задание №5
Нужно написать сквозной тест с использованием Selenium, который авторизует пользователя на сайте https://www.saucedemo.com/.

Данные для входа - логин: "standard_user", пароль: "secret_sauce".

Проверить, что авторизация прошла успешно и отображаются товары.


Вам необходимо использовать WebDriver для открытия страницы и методы sendKeys() для ввода данных в поля формы, и submit() для отправки формы. После этого, проверьте, что на странице 
отображаются продукты (productsLabel.getText() = "Products").

## Домашнее задание

## Задание 1
Представьте, что вы работаете над разработкой простого приложения для записной книжки, которое позволяет пользователям добавлять, редактировать и удалять контакты.

Ваша задача - придумать как можно больше различных тестов (юнит-тесты, интеграционные тесты, сквозные тесты) для этого приложения. Напишите название каждого теста, его тип и краткое описание того, что этот тест проверяет.

## Задание 2
Ниже список тестовых сценариев. Ваша задача - определить тип каждого теста (юнит-тест, интеграционный тест, сквозной тест) и объяснить, почему вы так решили.
* Проверка того, что функция addContact корректно добавляет новый контакт в список контактов".
* "Проверка того, что при добавлении контакта через пользовательский интерфейс, контакт корректно отображается в списке контактов".
* "Проверка полного цикла работы с контактом: создание контакта, его редактирование и последующее удаление".

# Семинар 6

## Задание №1
Напишите функцию для поиска среднего значения в списке чисел и соответствующие юниттесты с использованием фреймворка pytest.
## Задание №2
Модифицируйте функцию find_average так, чтобы она вызывала исключение TypeError, если ей передается не список.

Напишите тест, который проверяет вызов этого исключения
## Задание №3
Создайте два класса: Person и Bank. Класс Person должен иметь метод transfer_money, который позволяет перевести деньги в Bank. Класс Bank должен иметь метод receive_money.

Напишите тесты, проверяющие корректность взаимодействия этих классов.
## Задание №4
В предыдущем задании используйте unittest.mock для создания мок-объекта Bank.

Напишите тест, в котором вы проверите, вызывается ли метод receive_money с правильным аргументом.
## Задание №5
Напишите функцию divide(a, b), которая возвращает результат деления a на b. Если b равно нулю, функция должна вызывать исключение ZeroDivisionError.

Напишите тест, который проверяет, что при попытке деления на ноль функция вызывает исключение ZeroDivisionError
## Задание №6
Напишите функцию multiply(a, b), которая возвращает произведение a и b.

Затем напишите параметризованный тест, который проверяет эту функцию на нескольких наборах данных.
## Задание №7
Напишите тест, который проверяет, что встроенная функция len возвращает корректную  длину строки
## Задание №8
Создайте функцию square(n), которая возвращает квадрат числа n.

Напишите doctest, который проверяет работу этой функции.
## Задание №9
Напишите функцию is_prime(n), которая проверяет, является ли число n простым. Простое число - это число, которое делится только на 1 и на себя.

Напишите параметризованный тест с использованием pytest.mark.parametrize, который проверяет эту функцию на нескольких наборах данных.

## Домашнее задание

Создайте программу на Python или Java, которая принимает два списка чисел и выполняет следующие действия:
1. Рассчитывает среднее значение каждого списка.
2. Сравнивает эти средние значения и выводит соответствующее сообщение:
* "Первый список имеет большее среднее значение", если среднее значение первого списка больше.
* "Второй список имеет большее среднее значение", если среднее значение второго списка больше.
* "Средние значения равны", если средние значения списков равны.
#### Приложение должно быть написано в соответствии с принципами объектно-ориентированного программирования.
#### Используйте Pytest (для Python) или JUnit (для Java) для написания тестов, которые проверяют правильность работы программы. Тесты должны учитывать различные сценарии использования вашего приложения.
#### Используйте pylint (для Python) или Checkstyle (для Java) для проверки качества кода.
#### Сгенерируйте отчет о покрытии кода тестами. Ваша цель - достичь минимум 90% покрытия.

### Нужно предоставить:
* Код программы
* Код тестов
* Отчет pylint/Checkstyle
* Отчет о покрытии тестами
* Объяснение того, какие сценарии покрыты тестами и почему вы выбрали именно эти сценарии.