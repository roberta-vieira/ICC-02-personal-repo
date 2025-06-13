# Import Active Directory modules to use AD cmdlets
Import-Module ActiveDirectory

# Import user data information from the CSV file into a variable
$users = Import-Csv ".\lab-18-users.csv"


Write-Output "`nCreating users in Active Directory`n"
# Loop through each row to gather the user's information and create the AD account
foreach ($user in $users){

    Write-Output $user

    $first_name = $user.'FirstName'
    $last_name = $user.'LastName'
    $username = $user.'Username'
    $department = $user.'Department'
    $password = ConvertTo-SecureString $user.'Password' -AsPlainText -Force
    $OU_path = "OU=",$department,",OU=Groups,DC=greenbloom,DC=local" -join ""
    
    Write-Output $OU_path

    # Create a new AD user with the information from the CSV file
    New-ADUser -Name "$first_name $last_name" -GivenName $first_name -Surname $last_name -UserPrincipalName $username -SamAccountName $username -Department $department -Path $OU_path -AccountPassword $password -ChangePasswordAtLogon $True -Enabled $True
}
