function yesbutton () { 
	var image = document.getElementById("beemo");

	if (image.src.match("happyBeemo.jpg")) { 
		image.src = "gameBeemo.jpg";
		console.log("changed to Game Beemo!")
	} else { 
		image.src = "happyBeemo.jpg";
		console.log("changed to happy Beemo!")
	}
}