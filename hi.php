<!DOCTYPE html>
<html lang="en">
<head>
<title>CoinAccept - Home Page</title>
<meta charset="UTF-8">
<meta name="description" content="CoinAccept Dashboard">
<meta name="keywords" content="CoinAccept Dashboard, unica, creative, html">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link href="img/favicon.ico" rel="shortcut icon" />

<link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet">

<link rel="stylesheet" href="css/bootstrap.min.css" />
<link rel="stylesheet" href="css/font-awesome.min.css" />
<link rel="stylesheet" href="css/themify-icons.css" />
<link rel="stylesheet" href="css/animate.css" />
<link rel="stylesheet" href="css/owl.carousel.css" />
<link rel="stylesheet" href="css/style.css" />
<!--[if lt IE 9]>
	  <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
	  <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
	<![endif]-->
</head>
<style>
.main-section {
    border-top: 80px solid black;
	height: 800px;
	padding-top: 160px;
	display: block;
	background-color: #f3f7f9;
	position: relative;
	overflow: hidden;
}

.hero-text {
	padding-top: 60px;
}

.hero-text h2 {
	font-size: 70px;
	margin-bottom: 35px;
}

.hero-text h2 span {
	color: #16d0c5;
}

.hero-text h4 {
	color: #75849a;
	font-size: 22px;
}

.hero-subscribe-form {
	margin-top: 50px;
	display: block;
}

.hero-subscribe-form input {
	width: 315px;
	border: 1px solid #ebebeb;
	background: #fff;
	height: 48px;
	padding: 0 25px;
	border-radius: 50px;
	font-family: "Futura", sans-serif;
	font-size: 16px;
	margin-right: 8px;
	margin-bottom: 20px;
}

@media only screen and (max-width: 767px) {
	.main-section {
		height: auto;
		padding-bottom: 100px;
		padding-top: 160px;
	}
}

@media (max-width: 1585px) {
	.header-section .site-btn {
		margin-left: 0;
	}
	.main-section,
	.page-info-section {
		background-position: right 30% top;
	}
}

@media (max-width: 1425px) {
	.header-section .site-btn {
		margin-left: 0;
		
	}
	.main-section,
	.page-info-section {
		background-position: right 30% top;
	}
}

@media only screen and (min-width: 768px) and (max-width: 991px) {
	.main-section {
	    border: 1px solid black;
		height: 730px;
		padding-top: 160px;
	}
}

@media only screen and (min-width: 992px) and (max-width: 1199px) {
	.menu-list li a {
		margin-right: 15px;
	}
	.main-section,
	
	.page-info-section {
	    border: 1px solid black;
		background-position: right 23% top;
	}
	.about-img {
		left: 0px;
		width: 480px;
	}
	.member {
		width: calc(33.333333% - 25px);
		margin-bottom: 30px;
	}
	.team-members {
		text-align: center;
	}
	.fact h2 {
		font-size: 45px;
		margin-right: 10px;
	}
</style>
<body>

<div id="preloder">
<div class="loader"></div>
</div>

<header class="header-section clearfix">
<div class="container-fluid">
<a href="/index.php" class="site-logo">
<img src="img/logo.png" alt="">
</a>
<div class="responsive-bar"><i class="fa fa-bars"></i></div>
<a href="/login.php" class="user"><i class="fa fa-user"></i></a>
<a href="/register.php" class="site-btn">Log Out</a>
<nav class="main-menu">
<ul class="menu-list">
<li><a href="#">Home</a></li>
<li><a href="#">api key</a></li>
<li><a href="#">profile</a></li>
<li><a href="#">Contact Us</a></li>
<li><a href="/setting.php">setting</a></li>
<li><a href="/signout.php">sign out</a></li>
</ul>
</nav>
</div>
</header>



<section class="main-section spad">
<div class="container">
<div class="section-title text-center">
<h2>Empowering the Future of Crypto with Coin<span>Accept</span> <br></h2>
<h4>Your Perfect Crypto Partner Securely bridging the gap between crypto and everyday transactions</h4>
<form class="hero-subscribe-from" action="register.php">
<input type="text" placeholder="Enter your email">
<button class="site-btn sb-gradients">Get Started</button>
</form>
</div>
<div class="col-md-6">
<img src="img/laptop.png" class="laptop-image" alt="">
</div>
</div>
</div>
</section>


<footer class="footer-section">
<div class="container">
<div class="row spad">
<div class="col-md-6 col-lg-3 footer-widget">
<img src="img/logo.png" class="mb-4" alt="">
<p>Your Perfect Crypto Partner Securely bridging the gap between crypto and everyday transactions.</p>
<span>
Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved <i class="fa fa-heart-o" aria-hidden="true"></i> 
</span>
</div>
<div class="col-md-6 col-lg-2 offset-lg-1 footer-widget">
<h5 class="widget-title">Resources</h5>
<ul>
<li><a href="#">Coins Overview</a></li>
<li><a href="#">Faq</a></li>
<li><a href="#">API documentation</a></li>
</ul>
</div>
<div class="col-md-6 col-lg-2 offset-lg-1 footer-widget">
<h5 class="widget-title">Quick Links</h5>
<ul>
<li><a href="https://www.blockchain.com/">BlockChain Explorer</a></li>
<li><a href="#">Contact Us</a></li>
</ul>
</div>

</div>
<div class="footer-bottom">
<div class="row">
<div class="col-lg-4 store-links text-center text-lg-left pb-3 pb-lg-0">

</div>
<div class="col-lg-8 text-center text-lg-right">
<ul class="footer-nav">

<li><a href="#">Terms of Use</a></li>
<li><a href="#">Privacy Policy </a></li>
<li><a href="#"><span class="__cf_email__" data-cfemail="99eaece9e9f6ebedd9faf6f4e9f8f7e0b7faf6f4">[email&#160;protected]</span></a></li>

</ul>
</div>
</div>
</div>
</div>
</footer>

<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script src="js/jquery-3.2.1.min.js"></script>
<script src="js/owl.carousel.min.js"></script>
<script src="js/main.js"></script>

<script async src="https://www.googletagmanager.com/gtag/js?id=UA-23581568-13"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-23581568-13');
</script>
</body>
</html>
