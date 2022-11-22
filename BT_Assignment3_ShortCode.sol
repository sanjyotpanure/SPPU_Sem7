pragma solidity ^0.5.8;

contract Banking{

    uint balance;
    constructor() public{
        balance = 100;
    }

    function getBalance() view public returns(uint){
        return balance;
    }
    function withdraw(uint amt) public returns(uint remainingBal){
        if (amt <= balance){
            balance = balance - amt;
        }
        return balance;
    }
    function deposit(uint amt) public returns(uint remainingBal){
        balance = balance + amt;
        return balance;
    }
}
 

//*************** Alternative Way *************
//***************** Program 2 *****************
pragma solidity ^0.6;
contract banking
{
    mapping(address=>uint) private user_account;
    function deposit(uint amount) public payable returns(string memory)
    {
        user_account[msg.sender] += amount;
        return "Deposited Successfully";
    }
    function withdraw(uint amount) public payable returns(string memory)
    {
        require(user_account[msg.sender]>amount,"Insufficient Balance");
        require(amount>0,"Amount should be more than zero");
        user_account[msg.sender]=user_account[msg.sender]-amount;
        return "Withdrawl Successful";
    }
    function user_balance() public view returns(uint)
    {
        return user_account[msg.sender];
    }
}
