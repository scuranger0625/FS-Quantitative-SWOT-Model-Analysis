
# 將函數修改為從input中輸入權重

def set_swot_weights_from_input():
    try:
        # 輸入每個SWOT的權重 
        strength_weight = float(input("請輸入Strengths（優勢）的權重: "))
        weakness_weight = float(input("請輸入Weaknesses（劣勢）的權重: "))
        opportunity_weight = float(input("請輸入Opportunities（機會）的權重: "))
        threat_weight = float(input("請輸入Threats（威脅）的權重: "))

        # 計算總權重
        total_weight = strength_weight + weakness_weight + opportunity_weight + threat_weight
        if total_weight != 1:
            print(f"警告: 權重總和應該為1，但當前總和為: {total_weight:.2f}")

        return {
            "Strengths": strength_weight,
            "Weaknesses": weakness_weight,
            "Opportunities": opportunity_weight,
            "Threats": threat_weight
        }
    except ValueError:
        print("輸入無效，請輸入數值。")

# 測試從input中輸入權重
weights = set_swot_weights_from_input()

# 輸出設定的權重
weights
