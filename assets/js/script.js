

var groceryList = new Array ();






function main() {
    
    
    
    var searchTerm = document.searchBar.searchQuery.value
    
    
    
    
    
    
    
    
    //Editing Prexisting Elements
    
    //Price
    
    
    
    
    
    
    
    
    
    
    
    var superstore = []
    var nofrills = []
    var metro = []
    
    
    
    document.getElementById('bodyList').style.visibility='visible';
    
    

    
    //Change Superstore
    document.getElementById("superstoreInfo").href = superstore[0];
    document.getElementById("superstoreInfo").innerHTML = searchTerm;
    document.getElementById("superstorePrice").innerHTML = superstore[1];
    
    
    //Change NoFrills
    document.getElementById("nofrillsInfo").href = nofrills[0];
    document.getElementById("nofrillsInfo").innerHTML = searchTerm;
    document.getElementById("nofrillsPrice").innerHTML = nofrills[1];
    
    //Change Metro
    document.getElementById("metroInfo").href = metro[0];
    document.getElementById("metroInfo").innerHTML = searchTerm;
    document.getElementById("metroPrice").innerHTML = metro[1];
    
    
    
    
    
    
   
    

    
    
    
    

}



function superstoreAdd() {
    
    
    groceryList.push(new Array ("SuperStore", document.getElementById("superstoreInfo").innerHTML, document.getElementById("superstorePrice").innerHTML))
    
    
    
    
 
    
    
}

function makeList() {
    
    var mytable ='<table class="table table-striped my-5"> <thead> <tr> <th scope="col">Grocery Store</th> <th scope="col">Item</th> <th scope="col">Price</th> </tr> </thead> <tbody>'
    
           
    for (var i=0; i<groceryList.length; i++) {
        
        mytable += "<tr>";
        
        for (var j=0; j<groceryList[i].length; j++) {  mytable += "<td>" + groceryList[i][j] + "</td>"; }
        mytable += "</tr>";
        
    
        
        
    }
    
    mytable += "</tbody> </table>";
    document.getElementById("grocery_table").innerHTML = mytable;
}

function nofrillsAdd() {
    
    
    
    groceryList.push(new Array ("No Frills", document.getElementById("nofrillsInfo").innerHTML, document.getElementById("nofrillsPrice").innerHTML))
    

}

function metroAdd() {
    groceryList.push(new Array ("Metro", document.getElementById("metroInfo").innerHTML, document.getElementById("metroPrice").innerHTML))
    
}


