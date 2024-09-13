import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# SWOT全域變數 從下面進行評分

#Strengths計算分數部分
profitability_score = 85  # 盈利能力
asset_utilization_score = 88  # 資產利用率
cash_flow_score = 75  # 現金流
market_share_score = 90  # 市場佔有率

#Weaknesses計算分數部分
debt_level_score = 70  # 負債水平
cost_efficiency_score = 65  # 成本效率
employee_turnover_score = 60  # 員工流失率
technology_gap_score = 50  # 技術差距

#Opportunities 計算分數部分
market_growth_score = 85  # 市場增長
innovation_potential_score = 80  # 創新潛力
customer_demand_score = 90  # 客戶需求
industry_trends_score = 75  # 行業趨勢

#Threats計算分數部分
competition_score = 80  # 競爭
regulatory_risks_score = 70  # 法規風險
economic_instability_score = 75  # 經濟不穩定
technological_disruption_score = 65  # 技術破壞性


# 將函數修改為從input中輸入權重
def set_swot_weights_from_input():
    try:
        # 輸入每個SWOT的權重 
        strength_weight = float(input("請輸入Strengths（優勢）的權重: "))
        weakness_weight = float(input("請輸入Weaknesses（劣勢）的權重: "))
        opportunity_weight = float(input("請輸入Opportunities（機會）的權重: "))
        threat_weight = float(input("請輸入Threats（威脅）的權重: "))

        # 計算總權重，允許一個很小的誤差範圍
        total_weight = strength_weight + weakness_weight + opportunity_weight + threat_weight
        if abs(total_weight - 1.0) > 1e-6:
            print(f"警告: 權重總和應該為1，但當前總和為: {total_weight:.6f}")

        return {
            "Strengths": strength_weight,
            "Weaknesses": weakness_weight,
            "Opportunities": opportunity_weight,
            "Threats": threat_weight
        }
    except ValueError:
        print("輸入無效，請輸入數值。")



# 定義Strengths的計算函數，現在使用用戶輸入的權重
def calculate_strengths(profitability, asset_utilization, cash_flow, market_share, 
                        profit_weight, asset_weight, cash_flow_weight, market_share_weight):
    total_strength = (profitability * profit_weight) + (asset_utilization * asset_weight) + \
                     (cash_flow * cash_flow_weight) + (market_share * market_share_weight)
    return total_strength

# 定義Weaknesses的計算函數
def calculate_weaknesses(debt_level, cost_efficiency, employee_turnover, technology_gap, 
                         debt_weight, cost_weight, turnover_weight, tech_gap_weight):
    total_weaknesses = (debt_level * debt_weight) + (cost_efficiency * cost_weight) + \
                       (employee_turnover * turnover_weight) + (technology_gap * tech_gap_weight)
    return total_weaknesses

# 定義Opportunities的計算函數
def calculate_opportunities(market_growth, innovation_potential, customer_demand, industry_trends, 
                            market_growth_weight, innovation_weight, demand_weight, trends_weight):
    total_opportunities = (market_growth * market_growth_weight) + (innovation_potential * innovation_weight) + \
                          (customer_demand * demand_weight) + (industry_trends * trends_weight)
    return total_opportunities

# 定義Threats的計算函數
def calculate_threats(competition, regulatory_risks, economic_instability, technological_disruption, 
                      competition_weight, regulatory_weight, economic_weight, tech_disruption_weight):
    total_threats = (competition * competition_weight) + (regulatory_risks * regulatory_weight) + \
                    (economic_instability * economic_weight) + (technological_disruption * tech_disruption_weight)
    return total_threats

# 定義 SWOT 分析類別
class SWOTAnalysis:
    def __init__(self):
        self.weights = None

    def get_weights(self):
        if self.weights is None:
            self.weights = set_swot_weights_from_input()  # 只輸入一次
        return self.weights

    def analyze(self):
        weights = self.get_weights()

        # 定義 SWOT 的標籤
        swot_labels = ['Strengths', 'Weaknesses', 'Opportunities', 'Threats']

        # SWOT 分數計算，使用用戶輸入的權重
        strengths_score = calculate_strengths(profitability_score, asset_utilization_score, cash_flow_score, market_share_score,
                                              weights['Strengths'], weights['Strengths'], weights['Strengths'], weights['Strengths'])
        weaknesses_score = calculate_weaknesses(debt_level_score, cost_efficiency_score, employee_turnover_score, technology_gap_score,
                                                weights['Weaknesses'], weights['Weaknesses'], weights['Weaknesses'], weights['Weaknesses'])
        opportunities_score = calculate_opportunities(market_growth_score, innovation_potential_score, customer_demand_score, industry_trends_score,
                                                      weights['Opportunities'], weights['Opportunities'], weights['Opportunities'], weights['Opportunities'])
        threats_score = calculate_threats(competition_score, regulatory_risks_score, economic_instability_score, technological_disruption_score,
                                          weights['Threats'], weights['Threats'], weights['Threats'], weights['Threats'])

        # 分數和權重
        swot_scores = [strengths_score, weaknesses_score, opportunities_score, threats_score]
        swot_weights = [weights['Strengths'], weights['Weaknesses'], weights['Opportunities'], weights['Threats']]

        # 創建長條圖
        plt.figure(figsize=(7, 5))
        plt.bar(swot_labels, swot_scores, color='skyblue')

        # 在每個長條上顯示分數和權重
        for i, (score, weight) in enumerate(zip(swot_scores, swot_weights)):
            plt.text(i, score + 1, f'Score: {score}\nWeight: {weight}', ha='center')

        plt.tight_layout()
        plt.show()

# 使用類別來進行分析
swot_analysis = SWOTAnalysis()
swot_analysis.analyze()
