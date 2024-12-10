import gym
import numpy as np
np.bool8 = bool #для корректной синхронизации версий
def test_environment():
    #создаем среду
    env = gym.make("Taxi-v3", render_mode="ansi").env
    print("Среда успешно создана!")

    #проверяем пространство состояний и действий
    print(f"Количество состояний: {env.observation_space.n}")
    print(f"Количество действий: {env.action_space.n}")

    #сбрасываем среду и визуализируем начальное состояние
    initial_state = env.reset()[0]
    print("Начальное состояние:")
    print(env.render())

    #выполняем несколько случайных действий
    for i in range(5):
        action = env.action_space.sample()
        next_state, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated

        print(f"\nШаг {i + 1}:")
        print(f"Действие: {action}")
        print(f"Новое состояние: {next_state}")
        print(f"Награда: {reward}")
        print(f"Эпизод завершён: {done}")
        print(env.render()) 

        if done:
            print("Эпизод завершён. Сброс среды.")
            env.reset()

    print("Тестирование среды завершено.")

test_environment()
