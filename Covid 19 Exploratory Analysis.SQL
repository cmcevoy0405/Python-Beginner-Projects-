/* Covid 19 Data Exploartion

Skills used: Joins, CTES, Temp tables, Windows Functions, Aggregate Functions, creating views, Converting Data Types

*/

select *
from portfolioproject..coviddeaths
where continent is not null
order by 3,4


--Selecting Data we are going to be starting with
select location, date, total_cases, new_cases, total_deaths, population
from portfolioproject..coviddeaths
order by 1,2

--convert varchar Data to float
alter table portfolioproject..coviddeaths
alter column total_deaths float 

--Total Cases vs Total Deaths
--Shows likelihood of dying if you contract Covid in your country
select location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as deathpercentage
from portfolioproject..coviddeaths
where location like '%Ireland%'
order by 1,2

--Total Cases vs Population
--Shows percentage of population infected with covid in youe country
select location, date, total_cases, population, (total_cases/population)*100 as deathpercentage
from portfolioproject..coviddeaths
where location like '%Ireland%'
order by 1,2

--Countries with highest infection rate comapred to population
select location, max(total_cases) as HighestInfectionCount, population, Max((total_cases/population))*100 as PercentofPopulationInfected
from portfolioproject..coviddeaths
group by location, population
order by PercentofPopulationInfected desc

--Countires with highest death count per population
select location, max(total_deaths) as TotalDeaths
from portfolioproject..coviddeaths
where continent is not null
group by location
order by TotalDeaths desc

--BY CONTINENT

--Continents with highest death count per population
select continent, max(total_deaths) as TotalDeaths
from portfolioproject..coviddeaths
where continent is not null
group by continent
order by TotalDeaths desc

--Global Numbers
select date, sum(new_cases) as total_new_cases, sum (new_deaths) total_new_deaths, 
case
	when sum(new_cases) = 0 then null
	else (sum(new_deaths)/ nullif(sum(new_cases), 0))*100
	end as death_rate_percentage
from portfolioproject..coviddeaths
where continent is not null and new_cases is not null and new_deaths is not null
group by date
order by 1,2


--convert new vaccinations from varchar to float
alter table portfolioproject..covidvaccinations
alter column new_vaccinations float 

--Total population vs Vaccinations
----Percentage of population that have recieved at least one covid vaccination
select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, sum(vac.new_vaccinations) over (partition by dea.location order by dea.location, dea.date) as rolling_people_vaccinated 
from portfolioproject..coviddeaths as dea
join portfolioproject..covidvaccinations as vac
	on dea.location=vac.location
	and dea.date=vac.date
where dea.continent is not null
order by 2, 3

--use CTE to query off of partition by in previous query
with popvsvac (continent, location, date, population, new_vaccinations, rolling_people_vaccinated)
as
(select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, sum(vac.new_vaccinations) over (partition by dea.location order by dea.location, dea.date) as rolling_people_vaccinated 
from portfolioproject..coviddeaths as dea
join portfolioproject..covidvaccinations as vac
	on dea.location=vac.location
	and dea.date=vac.date
where dea.continent is not null
--order by 2, 3
)
select*, (rolling_people_vaccinated/population)*100 as percentage_of_pop_vaccinated
from popvsvac

--use temp table for same example
drop table if exists #percentpopulationvaccinated 
create table #percentpopulationvaccinated 
(
continent nvarchar(255),
location nvarchar(255),
date datetime,
population numeric,
new_vaccination numeric,
rolling_people_vaccinated numeric
)

insert into #percentpopulationvaccinated 
select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, sum(vac.new_vaccinations) over (partition by dea.location order by dea.location, dea.date) as rolling_people_vaccinated 
from portfolioproject..coviddeaths as dea
join portfolioproject..covidvaccinations as vac
	on dea.location=vac.location
	and dea.date=vac.date
where dea.continent is not null
--order by 2, 3
select*, (rolling_people_vaccinated/population)*100
from #percentpopulationvaccinated;


--Creating view to store data for later visualisations
create view percent_population_vaccinated as
select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, sum(vac.new_vaccinations) over (partition by dea.location order by dea.location, dea.date) as rolling_people_vaccinated 
from portfolioproject..coviddeaths as dea
join portfolioproject..covidvaccinations as vac
	on dea.location=vac.location
	and dea.date=vac.date
where dea.continent is not null
--order by 2, 3



