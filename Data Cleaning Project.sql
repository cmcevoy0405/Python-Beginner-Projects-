select *
from portfolioproject..housing

--change saledate
alter table housing
alter column
saledate Date

select saledate
from housing

--Populate propery address
select *
from portfolioproject..housing
order by parcelID

select a.parcelid, a.propertyaddress, b.parcelid, b.propertyaddress, isnull(a.propertyaddress, b.propertyaddress)
from portfolioproject..housing as a
join portfolioproject..housing as b	
	on a.parcelid = b.parcelid
	and a.uniqueid <> b. uniqueid
where a.propertyaddress is null

update a
set propertyaddress = isnull(a.propertyaddress, b.propertyaddress)
from portfolioproject..housing as a
join portfolioproject..housing as b	
	on a.parcelid = b.parcelid
	and a.uniqueid <> b. uniqueid
where a.propertyaddress is null

--segregating property address into address, city, state
select *
from portfolioproject..housing

select
SUBSTRING(propertyaddress, 1, charindex(',', propertyaddress)-1) as address
,SUBSTRING(propertyaddress, charindex(',', propertyaddress)+1, len(propertyaddress)) as city
from portfolioproject..housing

alter table housing
add propertysplitaddress nvarchar(255)

update housing
set propertysplitaddress = SUBSTRING(propertyaddress, 1, charindex(',', propertyaddress)-1) 

alter table housing 
add propertysplitcity nvarchar(255)

update housing
set propertysplitcity = SUBSTRING(propertyaddress, charindex(',', propertyaddress)+1, len(propertyaddress)) 

  

 select
 parsename(replace(owneraddress, ',', '.'), 3),
 parsename(replace(owneraddress, ',', '.'), 2),
 parsename(replace(owneraddress, ',', '.'), 1)
 from portfolioproject..housing

alter table portfolioproject..housing
add ownersplitaddress nvarchar(255)

update portfolioproject..housing
set ownersplitaddress =  parsename(replace(owneraddress, ',', '.'), 3)

alter table portfolioproject..housing 
add ownersplitcity nvarchar(255)

update portfolioproject..housing
set ownersplitcity =  parsename(replace(owneraddress, ',', '.'), 2)

alter table portfolioproject..housing 
add ownersplitstate nvarchar(255)

update portfolioproject..housing
set ownersplitstate =  parsename(replace(owneraddress, ',', '.'), 1)

select *
from portfolioproject..housing

--Changing Y and N to Yes and No in the "sold as vacant" field
select distinct(soldasvacant), count(soldasvacant)
from portfolioproject..housing
group by SoldAsVacant
order by 2

select soldasvacant,
case when SoldAsVacant = 'Y' then 'Yes'
	when SoldAsVacant = 'N' then 'No'
	else SoldAsVacant
end
from portfolioproject..housing

update portfolioproject..housing
set SoldAsVacant = 
case when SoldAsVacant = 'Y' then 'Yes'
	when SoldAsVacant = 'N' then 'No'
	else SoldAsVacant
end
from portfolioproject..housing;

--remove duplicates 
WITH RowNumCTE AS(
Select *,
	ROW_NUMBER() OVER (
	PARTITION BY ParcelID,
				 PropertyAddress,
				 SalePrice,
				 SaleDate,
				 LegalReference
				 ORDER BY
					UniqueID
					) row_num

From PortfolioProject.dbo.Housing
)
 select *
 from RowNumCTE
 where row_num >1 

 --delete unused columns
 select *
 from portfolioproject..housing

 alter table portfolioproject..housing
 drop column owneraddress, taxdistrict, propertyaddress 


 