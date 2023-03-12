setTimeout(() => {document.getElementById("hide").innerHTML = "I look forward to working together"}, 3000);

let titles = ["I am excited to help you", "Feel free to reach me out", "I am willing to hear the details!"];
let currentIndex = 0;
let ct = document.getElementsByClassName("contact-text");

setInterval(() => {
   
    ct.innerHTML= titles[currentIndex];   
   
   currentIndex++;
   
   if (currentIndex === 3)
    currentIndex = 0;

}, 2000)

$('.nav-link').on('click', function() {
	$('.active-link').removeClass('active-link');
	$(this).parent().addClass('active-link');
});