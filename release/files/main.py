from fermat_test import run_feramn_test
from sol_stra_test import run_solovay_strassen_test
from mill_rab_test import run_miller_rabin_test

if __name__ == "__main__":
    try: 
        n_input = input("enter n: ")
        n = int(n_input)
        t_input = input ("enter t: ")
        t = int(t_input)

        if n < 5 or n % 2 == 0:
            print(f"Ошибка: {n} должно быть нечетным целым числом >= 5.")
            if n == 2 or n == 3:
                print(f"{n} - простое число.")
            elif n % 2 == 0:
                print(f"{n} - составное число (четное).")
        elif t < 1:
            print("Ошибка: количество итераций t должно быть >= 1.")
        else:
            print(f"\n--- Тестирование числа {n} (c {t} итерациями) ---")

            result_fermat = run_feramn_test(n, t)
            print(f"1. Тест Ферма: \t\t{result_fermat}")

            result_ss = run_solovay_strassen_test(n, t)
            print(f"2. Тест Соловэя-Штрассена: \t{result_ss}")

            result_mr = run_miller_rabin_test(n, t)
            print(f"3. Тест Миллера-Рабина: \t{result_mr}")

            print("\n--- Вывод ---")
            if result_mr == "probably prime":
                print(f"Число {n}, вероятно, простое.")
                print(f"(Вероятность ошибки < 1 / (4^{t}))") 
            else:
                print(f"Число {n} - составное.")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректные целые числа.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")