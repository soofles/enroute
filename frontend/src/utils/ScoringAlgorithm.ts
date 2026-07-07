import type { Stop } from "../types/Stop"
import type { Travel } from "../types/Travel"

interface TripScore {
    overallScore: number;
    planningScore: number;
    budgetingScore: number;
    completenessScore: number;
}

export function getTripScore(stops: Stop[], travels: Travel[], budget: number): TripScore {
    const planningScore = getPlanningScore(stops, travels);
    const budgetingScore = getBudgetingScore(stops, budget);
    const completenessScore = getCompletenessScore(stops);
    return {
        overallScore: Math.round(planningScore * 0.4 + budgetingScore * 0.3 + completenessScore * 0.3),
        planningScore: planningScore,
        budgetingScore: budgetingScore,
        completenessScore: completenessScore,
    }
}

export function getPlanningScore(stops: Stop[], travels: Travel[]): number {
    return 50;
}

export function getBudgetingScore(stops: Stop[], budget: number): number {
    return 80;
}

export function getCompletenessScore(stops: Stop[]): number {
    return 20;
}