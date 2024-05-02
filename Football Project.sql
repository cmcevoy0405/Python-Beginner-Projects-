
--Using a case statment to class goal scorers throughout the league
select full_name, [current club], goals_overall,
case 
	when goals_overall >= 18 then 'Proflific scorer'
	when goals_overall >= 10 then 'Average scorer'
	else 'Low scorer' 
end as scorer_ranking
from portfolioproject..players
order by goals_overall desc

--Using a CTE and window fucntions to identify the top scorer in each team
with scoringrank as
(
select full_name , goals_overall, [Current Club],
ROW_NUMBER() over (partition by [current club] order by goals_overall desc) team_rank
from portfolioproject..players
) 
select * 
from scoringrank
where team_rank <= 1
order by goals_overall desc

--using a subquery instead
select full_name, goals_overall, [Current Club]
from (
select full_name , goals_overall, [Current Club],
ROW_NUMBER() over (partition by [current club] order by goals_overall desc) team_rank
FROM portfolioproject..players) as ranked_players
where team_rank <=1

--Percentage of goals scored by top player contributing to overall team score
create table #TopScorerPerTeam 
(full_name nvarchar (225),
goals_overall int,
Club nvarchar (225),
team_goals int,
)
	
INSERT INTO #TopScorerPerTeam 
SELECT distinct p.full_name, p.goals_overall, p.[Current Club], t.goals_scored
FROM (
    SELECT full_name, goals_overall, [Current Club], season,
           ROW_NUMBER() OVER (PARTITION BY [Current Club] ORDER BY goals_overall desc, [current club] DESC) AS team_rank
    FROM portfolioproject..players
) AS p
JOIN portfolioproject..teams AS t ON p.[Current Club] = t.common_name
WHERE p.team_rank = 1
	
select *
from #TopScorerPerTeam
order by 4 desc

--contribution the top scorer from each team has to team goals
select full_name, goals_overall, club, team_goals, round(cast(goals_overall as float) / team_goals, 4)*100 as Percentage_contribution_to_team
from #TopScorerPerTeam
order by Percentage_contribution_to_team desc

--highest scoring nation
select sum(goals_overall) as goals, nationality
from portfolioproject..players
group by nationality
order by goals desc

--Ranking Teams based on goals
select team_name, goals_scored, league_position,
rank() over (order by goals_scored desc) as ranking
from portfolioproject..teams

--Finding avg goals per match
select team_name, goals_scored, round(goals_scored/matches_played, 3) as goals_per_game
from portfolioproject..teams
order by 3 desc

--Finding best keeper
select top 1 full_name, position, [Current Club], clean_sheets_overall
from portfolioproject..players
where position like '%goalkeeper%'
order by clean_sheets_overall desc



--