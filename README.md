
<h1 align="center"><a href="https://h3llcodes.pythonanywhere.com" target="_blank">Xmeme</a></h1>
  
Xmeme is a WebApp where people can share memes, some fun moments with other people without any need to login and singup. You just spread happiness 😁

<h3>Some Key Features of Xmeme App:</h3>
<ul>
  <li> You do not need to sign up to share your memes</li>
  <li> Enter the meme url, url can contain all image types including support for gifs</li>
  <li> Well want to edit the meme url, you are free to do so hit the edit meme button and you are good to go</li>
  <li> You can use it from your desktop or from the comfort of your mobile device (Resposnive Design and Layout)</li>
  <li></li>
  <li></li>
</ul>

<h3><a href="https://h3llcodes.pythonanywhere.com/memes" target="_blank">Xmeme API</a>:</h3>
<p>
If simply uploading details in a form does not satisfy your desire well I got you covered 😎 Xmeme has an inbuilt API which you can use to GET list of all the memes currently in the system, POST meme from your terminal, Oh yes! now that is some action right there. You can also edit the memes with the help of API using the patch request
  
<h3>Using the API (curl commands):</h3>
<ul>
  <li><b>GET request 👇</b> <p> curl -i --location --request GET https://h3llcodes.pythonanywhere.com/memes</p></li>

  <li><b>POST request 👇</b>  <p>curl --location --request POST https://h3llcodes.pythonanywhere.com/memes --header Content-Type:application/json --data-raw "{\"name\":\"ashok kumar\",  \"url\":\"https://media.tenor.com/images/c51500433e6f6fff5a8c362335bc8242/tenor.gif\",  \"caption\":\"This is a meme\"}"</p> </li>
  
  <li><b>PATCH request 👇</b>  <p>curl -i --location --request PATCH  https://h3llcodes.pythonanywhere.com/memes/51 --header Content-Type:application/json --data-raw "{\"url\":\" https://media.tenor.com/images/c66854d3abac1c03b62676eedfc8d2e2/tenor.gif \",  \"caption\":\"hell yeah we are using patch request\"}"</p> </li>
  
</ul>

<h1 align="center">YouTube Demo Video</h1>

<p align="center">
  <a href="https://youtu.be/4bmlVy1W9Y0" target="_blank"><img src="https://github.com/divy-14/Data-structures-and-Algorithms/blob/master/Result_images/xmeme_logo.gif" alt="demo Xmeme" width="600px" height="400px"></a>
</p>

<h1 align="center">Found a Bug</h1>
<p> 
If you find any bug or have any feature request, feel free to raise an issue or contact me on : <a href="mailto:divymohanrai@gmail.com"> Divy Mohan Rai </a>, 
If you want to contribute to this project please create a pull request.
</p>

#### If you liked ♥ this project, please hit that **STAR** button.
