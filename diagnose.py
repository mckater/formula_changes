# diagnose.py
import sys
from typing import Dict, List, Tuple

from flask import jsonify, request


def calculate_change_readiness(D: int, V: int, F: int, R: int) -> Dict:
    """Возвращает результат диагностики по формуле C = D × V × F > R"""
    product = (D * V * F) / 100.0
    assessment = ""
    recommendation = ""
    status = ""

    if product > R:
        assessment = "готов(-а) к старту"
        status = "ready"
        recommendation = "Импульс есть — запускайте первые шаги и переходите в режим видения (V)."
    elif abs(product - R) <= 0.5:
        assessment = "на грани — требуется поддержка"
        status = "edge"
        recommendation = "Можно стартовать, но добавьте: наставника, микрошаги, чек-лист или союзника."
    else:
        assessment = "пока не готов(-а)"
        status = "not_ready"
        recommendation = "Сначала усильте слабое звено (D, V или F), прежде чем начинать."

    # Определяем слабое звено
    factors = {'D': D, 'V': V, 'F': F}
    weakest = min(factors, key=factors.get)
    weakest_val = factors[weakest]
    weakest_names = {
        'D': 'неудовлетворённость',
        'V': 'видение',
        'F': 'первые шаги'
    }

    suggested_actions = {
        'D': [
            "Выписать 3 реальные потери от статус-кво за последний месяц",
            "Описать сценарий «ничего не меняю» через 1 год — в деталях",
            "Послушать подкаст/интервью человека, прошедшего похожий путь"
        ],
        'V': [
            "Описать «идеальный день» через 1 год: утро → вечер",
            "Заполнить шаблон: «Я человек, который ________»",
            "Найти 1 кейс человека с похожей целью"
        ],
        'F': [
            "Определить 1 микрошаг: действие + время + место + ≤20 мин",
            "Заблокировать 25 минут завтра в календаре",
            "Подготовить всё необходимое заранее (скрипт, заметки и т.д.)"
        ]
    }[weakest]

    return {
        "product": round(product, 2),
        "R": R,
        "assessment": assessment,
        "status": status,
        "recommendation": recommendation,
        "weakest_factor": weakest,
        "weakest_name": weakest_names[weakest],
        "weakest_value": weakest_val,
        "suggested_actions": suggested_actions
    }


def cli_main():
    """Запуск из терминала: python diagnose.py"""
    print("=== ФОРМУЛА ИЗМЕНЕНИЙ: Самодиагностика (CLI) ===")
    try:
        D = int(input("D (неудовлетворённость, 0–10): "))
        V = int(input("V (видение, 0–10): "))
        F = int(input("F (первые шаги, 0–10): "))
        R = int(input("R (сопротивление, 0–10): "))
    except ValueError:
        print("❌ Ошибка: введите целые числа от 0 до 10.")
        sys.exit(1)

    if not all(0 <= x <= 10 for x in (D, V, F, R)):
        print("❌ Все значения должны быть от 0 до 10.")
        sys.exit(1)

    result = calculate_change_readiness(D, V, F, R)

    print("\n" + "="*50)
    print(f"D × V × F / 100 = {result['product']} | R = {result['R']}")
    print(f"Статус: {result['assessment'].upper()}")
    print(f"Рекомендация: {result['recommendation']}")
    print(f"Слабое звено: {result['weakest_factor']} — {result['weakest_name']} ({result['weakest_value']}/10)")
    print("\n3 микрошага для усиления:")
    for i, a in enumerate(result['suggested_actions'], 1):
        print(f"  {i}. {a}")
    print("="*50)


# === Flask-эндпоинт (если используется в приложении) ===
def add_diagnosis_routes(app):
    """Добавляет /api/diagnose POST-эндпоинт в Flask-приложение"""
    @app.route('/change_diagnosis', methods=['POST'])
    def api_diagnose():
        data = request.get_json()
        try:
            D = int(data['D'])
            V = int(data['V'])
            F = int(data['F'])
            R = int(data['R'])
            if not all(0 <= x <= 10 for x in (D, V, F, R)):
                return jsonify({"error": "All values must be 0–10"}), 400
        except (KeyError, ValueError, TypeError):
            return jsonify({"error": "Invalid input: provide D, V, F, R as integers 0–10"}), 400

        result = calculate_change_readiness(D, V, F, R)
        result['goal'] = data.get('goal', '')
        return jsonify(result)


# Запуск как скрипт
if __name__ == '__main__':
    cli_main()