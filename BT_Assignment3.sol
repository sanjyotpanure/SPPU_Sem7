pragma solidity ^0.4.25;

contract Banking{

    uint balance;
    address private owner;

    constructor() public{
        balance = 10;
        owner = msg.sender;
    }

    function getOwner() public view returns (address) {	
		return owner;
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
