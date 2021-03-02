const presetAmount = document.querySelector('#presetAmount');
const userAmount = document.querySelector('#userAmount');
const donationTotal = document.querySelector('.donationTotal');

presetAmount.onchange = (e) => updateUserDonation(e, 'preset')
userAmount.onkeyup = (e) => updateUserDonation(e, 'user')
userAmount.onchange = (e) => updateUserDonation(e, 'user')

// change preset amount to none (0 index = no int value) if preset amount selected
const updateUserDonation = (e, option) => {

    option === 'preset'
        ? userAmount.value = ""
        : presetAmount.selectedIndex = "0"

    // get total value from user entered option
    donationTotal.value = e.target.value;
    console.log(donationTotal.value)

    // get total and return as HTML string 
    document.getElementById('displayAmount').innerHTML = donationTotal.value;
}
