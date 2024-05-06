import requests
from bs4 import BeautifulSoup, NavigableString
import pandas as pd

# Tu HTML como una string
html_content = '''<html lang="es"><head lang="es">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<style type="text/css">
<!--
.sprite-spanish { border: solid 0px;margin-top:0px;float:left;display:block;padding-right:4px;background: url(//static.vocabulix.com/images/conjugation/sprite-spanish.png) no-repeat top left; }
-->
</style>
<link rel="stylesheet" type="text/css" href="/css/vocabulix6.css">
<style type="text/css">
.conjLowerResponsive {display:inline-block;width:300px;height:250px;}
.conjBox1Responsive {display:inline-block;width:300px;height:250px;}
.conjQueryResponsive {display:inline-block;width:300px;height:600px;}
@media only screen and (max-width: 900px) {
	 .conjLowerResponsive {display:inline-block;width:300px;height:250px;}
	 .conjBox1Responsive {display:inline-block;width:320px;height:100px;}
	 .conjQueryResponsive {display:inline-block;width:320px;height:100px;}
}
</style>
<style type="text/css">
div.specificTenseWrapper {margin-top:30px;background:#f5f5f5;}
span.specificTenseHead {font-size:22px;}
div.conjUpperBoxRight {position:relative;}
div.nextVerbs2, div.drillBox2, div.conjTranslation, div.specificTenseWrapper, div.videoHolder2,div.newsletter2
	{border: solid 1px #8c8c8c; padding:10px 8px;-webkit-border-radius: 20px;-moz-border-radius: 20px;border-radius: 20px;}
div.nextVerbs2 {margin:30px 10px;background:#DCE9BE;font-size:18px;}
div.drillBox2 {float:right;width:280px;font-size:20px;background:#f5f5f5;color:#8c8c8c;margin:0px;margin-top:40px;font-weight:bold;}
div.videoHolder2 { margin: 30px 10px;text-align:center;background:black; }
div.newsletter2 {display:none;}
div.conjTranslation {width:280px;margin:30px 0px 0px 0px;}
div.searchPromDiv {vertical-align:bottom;display: table-cell;padding:3px;}
div.searchPromDiv:after {content:'Advertisement';font-weight:bold;}
@media only screen and (max-width: 900px) {
	div.nextVerbs2, div.drillBox2, div.conjTranslation, div.specificTenseWrapper, div.videoHolder2,div.newsletter2
	{border: none; padding:10px;-webkit-border-radius: 0px;-moz-border-radius: 0px;border-radius: 0px;}
	div.nextVerbs2, div.drillBox2 {width:281px;margin:20px 0px;}
	div.videoHolder2 { margin: 30px 0px;padding:0px; }
	div.specificTenseWrapper {margin-bottom:15px;background:#f5f5f5;}
	div.conjTranslation {  width:280px; }
	span.specificTense {font-size:16px;}
	span.specificTenseHead {font-size:18px;}
	div.specificTenseCell {width:125px;}
	div.searchPromDiv:after {content:'';}
}
</style>
<meta name="viewport" content="initial-scale=1.0, user-scalable=no">
<link rel="manifest" href="/misc/manifest/manifest-Verbos-Espanol.json">

<title>Conjugación de activar</title>
<meta name="description" content="Conjugación de Activar en español. Aprende cómo conjugar el verbo activar en tiempos diferentes. Presente: yo activo, tú activas, él activa ...">
<meta name="keywords" content="activar">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="-1">
<meta property="fb:app_id" content="123927337650188">
<meta property="og:image" content="http://www.vocabulix.com/images/logo220t.png">
<script src="/js/functions/verbPostLoad-2.js" type="text/javascript" async=""></script><script src="https://pagead2.googlesyndication.com/pagead/managed/js/adsense/m202403250101/reactive_library_fy2021.js"></script><script src="https://pagead2.googlesyndication.com/pagead/managed/js/adsense/m202403250101/show_ads_impl_with_ama_fy2021.js?client=ca-pub-3415784549533464&amp;plah=www.vocabulix.com&amp;aplac=true"></script><script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('consent', 'default', {'ad_storage': 'denied','ad_user_data': 'denied','ad_personalization': 'denied','analytics_storage': 'denied','functionality_storage': 'denied','security_storage': 'granted','wait_for_update': 2000});
</script>
<script async="" src="https://www.googletagmanager.com/gtag/js?id=G-GPCJ4RZP19"></script>
<script>window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());gtag('config', 'G-GPCJ4RZP19');
var _gaq = _gaq || [];
</script>
 <script async="" src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">
</script>
<style>
.sprite-1_spanish { background-position: 0 0; width: 13px; height: 10px; }
.sprite-1e_spanish { background-position: 0 -60px; width: 15px; height: 8px; }
.sprite-2_spanish { background-position: 0 -118px; width: 11px; height: 11px; }
.sprite-2e_spanish { background-position: 0 -179px; width: 11px; height: 10px; }
.sprite-3_spanish { background-position: 0 -239px; width: 10px; height: 11px; }
.sprite-3e_spanish { background-position: 0 -300px; width: 13px; height: 8px; }
.sprite-4_spanish { background-position: 0 -358px; width: 44px; height: 10px; }
.sprite-4e_spanish { background-position: 0 -418px; width: 19px; height: 8px; }
.sprite-5_spanish { background-position: 0 -476px; width: 44px; height: 10px; }
.sprite-5e_spanish { background-position: 0 -536px; width: 13px; height: 8px; }
.sprite-6_spanish { background-position: 0 -594px; width: 24px; height: 10px; }
.sprite-6e_spanish { background-position: 0 -654px; width: 13px; height: 8px; }
.sprite-GENERAL_CONDITIONAL_spanish { background-position: 0 -712px; width: 66px; height: 11px; }
.sprite-GENERAL_FUTURE_spanish { background-position: 0 -773px; width: 38px; height: 11px; }
.sprite-GENERAL_PAST_2_spanish { background-position: 0 -834px; width: 114px; height: 11px; }
.sprite-GENERAL_PAST_spanish { background-position: 0 -895px; width: 101px; height: 27px; }
.sprite-GENERAL_PERFECT_1_spanish { background-position: 0 -972px; width: 166px; height: 13px; }
.sprite-GENERAL_PERFECT_spanish { background-position: 0 -1035px; width: 100px; height: 26px; }
.sprite-GENERAL_PRESENT_spanish { background-position: 0 -1111px; width: 55px; height: 12px; }
</style>
<meta http-equiv="origin-trial" content="As0hBNJ8h++fNYlkq8cTye2qDLyom8NddByiVytXGGD0YVE+2CEuTCpqXMDxdhOMILKoaiaYifwEvCRlJ/9GcQ8AAAB8eyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3MTk1MzI3OTksImlzU3ViZG9tYWluIjp0cnVlfQ=="><meta http-equiv="origin-trial" content="AgRYsXo24ypxC89CJanC+JgEmraCCBebKl8ZmG7Tj5oJNx0cmH0NtNRZs3NB5ubhpbX/bIt7l2zJOSyO64NGmwMAAACCeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3MTk1MzI3OTksImlzU3ViZG9tYWluIjp0cnVlfQ=="><meta http-equiv="origin-trial" content="A/ERL66fN363FkXxgDc6F1+ucRUkAhjEca9W3la6xaLnD2Y1lABsqmdaJmPNaUKPKVBRpyMKEhXYl7rSvrQw+AkAAACNeyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiRmxlZGdlQmlkZGluZ0FuZEF1Y3Rpb25TZXJ2ZXIiLCJleHBpcnkiOjE3MTkzNTk5OTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="A6OdGH3fVf4eKRDbXb4thXA4InNqDJDRhZ8U533U/roYjp4Yau0T3YSuc63vmAs/8ga1cD0E3A7LEq6AXk1uXgsAAACTeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiRmxlZGdlQmlkZGluZ0FuZEF1Y3Rpb25TZXJ2ZXIiLCJleHBpcnkiOjE3MTkzNTk5OTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><style type="text/css">
@font-face {
  font-weight: 400;
  font-style:  normal;
  font-family: circular;

  src: url('chrome-extension://liecbddmkiiihnedobmlmillhodjkdmb/fonts/CircularXXWeb-Book.woff2') format('woff2');
}

@font-face {
  font-weight: 700;
  font-style:  normal;
  font-family: circular;

  src: url('chrome-extension://liecbddmkiiihnedobmlmillhodjkdmb/fonts/CircularXXWeb-Bold.woff2') format('woff2');
}</style></head>
<body onload="if(window.verbOnLoad) verbOnLoad('s','s','http://www.vocabulix.com/conjugacion/Verbos-Espanol.html');" class="clickup-chrome-ext_installed" cz-shortcut-listen="true" style="padding: 0px;">
<script type="text/javascript">
SYS_LANG='spanish';
OTH_LANG='spanish';
SL='s';
OL='s';
FOLDER_NAME='conjugacion3';

</script>
<div class="mainWrapper mainWrapperMinHeightConj"><div class="newpanelLeft panelLeftThin" id="newpanelLeftID"><div class="menubckNEW"><div class="logobuttonNEWWrapper" id="logobuttonNEWWrapper"><div class="logobuttonNEW">Vocabulix</div><div class="mobMenuBtn" onclick="openCloseMenu();"></div></div><div id="menuInnerID" class="menuInner menuInnerConjDict">
<div class="menuBlock"><a class="newmenuNEW" target="_top" href="/indexSP.shtml"><script language="javascript" type="text/javascript"><!--
document.write('Inicio');

// -->
</script>Inicio
</a></div>
<div class="menuBlock"><a class="newmenuNEW" href="/conjugacion/Verbos-Espanol.html">Verbos en español</a></div>
<div class="menuBlock"><a class="newmenuNEW" href="/online/Aprender/Verbos">Ejercicios de verbos</a></div>
<div class="menuBlock"><a class="newmenuNEW" href="/online/Aprender/Espanol">Aprender español</a></div>
<div class="menuBlock"><a class="newmenuNEW" href="/online/Aprender/Vocabulario">Aprender vocabulario español</a></div>
<div class="menuBlock loadMenuBtn" id="loadMenuBtnID" onclick="loadFullMenu();"></div><div id="skyAnchorId" class="skyAnchor"><div class="logosmalltext">Aprender español online
</div></div></div></div></div><div class="newpanelRight generalRightSideWidth panelRightThin" id="newpanelRightID">
<div class="loginWrapper" id="loginPlaceHolderID"><form action="/online/servlet/eTranslator.MainServlet" name="dynLoginForm" id="dynLoginForm" class="formStyle" method="post"><input type="hidden" name="eventName" value=""><input type="hidden" name="lang" value="2"><div class="menuDropDownLev1"><input class="button-link-login" type="button" onclick="genericSubmit('showForceLogin', document.dynLoginForm);" value="Registrarse"><br><input class="loginButtonNEW hideOnMini" type="button" value="Nuevo usuario >" onclick="genericSubmit('showForceLogin', document.dynLoginForm);"></div></form></div>
<div class="mainPanel mainPanelConjDictPatch" id="mainPanelID">
<span class="welcomeNote">
<script language="javascript" type="text/javascript">

<!--

document.write('Aqu&#237; encontrar&#225;s la conjugaci&#243;n del verbo "activar". Elige el tiempo verbal deseado de la lista siguiente, o haz clic en uno de los v&#237;nculos al final de este cuadro para ver tiempos verbales espec&#237;ficos.');

// -->

</script>Aquí encontrarás la conjugación del verbo "activar". Elige el tiempo verbal deseado de la lista siguiente, o haz clic en uno de los vínculos al final de este cuadro para ver tiempos verbales específicos.

</span>
<a name="soundWindowAnchor"></a><div class="soundWinDict" id="soundWindow"></div><div class="conjUpperBoxWrapper"><div class="upperPaneDiv" id="upperPaneDiv"></div><div class="conjUpperBoxRight"><div class="conjPromoDiv"><div class="plusoneDiv" id="plusonespan"></div><div class="likeTwitterDiv" id="twitterPromoDiv"></div><div class="likePromoDiv" id="likePromoDiv"></div><div class="likeExtraDiv" id="likeExtraDiv"></div>
</div>
<div class="searchPromDiv" id="searchPromDiv">&nbsp;</div>
<!-- Conjugation Asynch ATF 300x250 -->
<ins class="adsbygoogle conjBox1Responsive" data-ad-client="ca-pub-3415784549533464" data-ad-slot="5743992731" data-adsbygoogle-status="done" style="width: 300px; height: 250px;" data-ad-status="filled"><div id="aswift_0_host" style="border: none; height: 250px; width: 300px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: inline-block;"><iframe id="aswift_0" name="aswift_0" style="left:0;position:absolute;top:0;border:0;width:300px;height:250px;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="300" height="250" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allow="attribution-reporting; run-ad-auction" src="https://pagead2.googlesyndication.com/pagead/ads?ltd_cs=1&amp;client=ca-pub-3415784549533464&amp;output=html&amp;h=250&amp;slotname=5743992731&amp;adk=2227698367&amp;adf=1127349287&amp;pi=t.ma~as.5743992731&amp;w=300&amp;abgtt=3&amp;lmt=1711871510&amp;rafmt=12&amp;format=300x250&amp;url=https%3A%2F%2Fwww.vocabulix.com%2Fconjugacion3%2Factivar.html&amp;wgl=1&amp;uach=WyJtYWNPUyIsIjEyLjcuMiIsIng4NiIsIiIsIjEyMy4wLjYzMTIuODciLG51bGwsMCxudWxsLCI2NCIsW1siR29vZ2xlIENocm9tZSIsIjEyMy4wLjYzMTIuODciXSxbIk5vdDpBLUJyYW5kIiwiOC4wLjAuMCJdLFsiQ2hyb21pdW0iLCIxMjMuMC42MzEyLjg3Il1dLDBd&amp;dt=1711875570110&amp;bpp=2&amp;bdt=178&amp;idt=21&amp;shv=r20240327&amp;mjsv=m202403250101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;eo_id_str=ID%3Dbb8f32e6ab7cfb3f%3AT%3D1711870727%3ART%3D1711875539%3AS%3DAA-AfjbnZc70O3pI3j4Vx3TFgXqN&amp;correlator=6372637868985&amp;frm=20&amp;pv=2&amp;ga_vid=347672392.1711875570&amp;ga_sid=1711875570&amp;ga_hid=1893198956&amp;ga_fc=0&amp;u_tz=120&amp;u_his=20&amp;u_h=900&amp;u_w=1440&amp;u_ah=875&amp;u_aw=1440&amp;u_cd=24&amp;u_sd=2&amp;dmc=8&amp;adx=801&amp;ady=187&amp;biw=1440&amp;bih=754&amp;scr_x=0&amp;scr_y=0&amp;eid=44759875%2C44759926%2C44759842%2C31081576%2C31082197%2C44795921%2C95326315%2C95329017%2C95322183%2C95328825%2C31078663%2C31078665%2C31078668%2C31078670&amp;oid=2&amp;pvsid=4425896326566574&amp;tmod=667825585&amp;uas=0&amp;nvt=1&amp;ref=https%3A%2F%2Fwww.vocabulix.com%2Fconjugacion2%2Fa_spanish.html&amp;fc=640&amp;brdim=0%2C25%2C0%2C25%2C1440%2C25%2C1440%2C875%2C1440%2C754&amp;vis=1&amp;rsz=%7Co%7CeE%7C&amp;abl=NS&amp;pfx=0&amp;fu=256&amp;bc=31&amp;bz=1&amp;td=1&amp;nt=1&amp;ifi=1&amp;uci=a!1&amp;fsb=1&amp;dtd=26" data-google-container-id="a!1" tabindex="0" title="Advertisement" aria-label="Advertisement" data-google-query-id="CNfYkbqRnoUDFeem0QQdlZoFww" data-load-complete="true"></iframe></div></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div><div class="conjUpperBoxLeft"><div class="headerTitleWrap"><div class="headerTitleLeftWrap"><span class="icon sprite-verbs"></span><h1 class="headerTitleIcon">Conjugación de "activar" en español</h1></div><div class="headerTitleRightWrap" id="headerTitleRightWrapID"></div><div class="clearer"></div></div><br>
<div class="chooseTenseWrapper"><form style="font-size:14px;font-weight:bold;" id="chooseForm" action="/"><span style="font-size:25px;color:#10a8ab">➜ </span><select class="chooseTense" id="selector" onchange="if(this.options[this.selectedIndex].value != '0') { document.location.href = '../conjugacion/query_spanish.html?conjugation3,activar,%22activar%22,' + this.options[this.selectedIndex].value; }">  <option value="0">Elige tiempo por "activar"
</option><option value="Presente">Presente
</option><option value="Pret%C3%A9rito%20perfecto%20compuesto">Pretérito perfecto compuesto
</option><option value="Pret%C3%A9rito%20imperfecto">Pretérito imperfecto
</option><option value="Pret%C3%A9rito%20pluscuamperfecto">Pretérito pluscuamperfecto
</option><option value="Pret%C3%A9rito%20perfecto%20simple">Pretérito perfecto simple
</option><option value="Pret%C3%A9rito%20anterior">Pretérito anterior
</option><option value="Futuro">Futuro
</option><option value="Futuro%20perfecto">Futuro perfecto
</option><option value="Presente%20Subjuntivo">Presente Subjuntivo
</option><option value="Pret%C3%A9rito%20perfecto%20Subjuntivo">Pretérito perfecto Subjuntivo
</option><option value="Futuro%20Subjuntivo">Futuro Subjuntivo
</option><option value="Futuro%20perfecto%20Subjuntivo">Futuro perfecto Subjuntivo
</option><option value="Condicional">Condicional
</option><option value="Condicional%20compuesto">Condicional compuesto
</option></select></form></div>
<div class="searchFormWrap"><form accept-charset="UTF-8" name="dictionaryForm" onsubmit="if(typeof validateBeforeSearch=='function') { return validateBeforeSearch('Ingresa otro verbo...','spanish'); } else return true; " action="/online/dict-conjugation.jsp" method="post"><table><tbody><tr><td>
<div id="outerTextFieldDiv" class="outerTextFieldDiv"><input id="conjsearchBox" autocomplete="off" onfocus="if(typeof onFocusDo=='function') { onFocusDo(this); } else this.value='';" class="searchInputBox" type="text" size="12" name="search" value="Ingresa otro verbo...">
<div id="divSuggest" class="divSuggest" style="z-index: 100000; top: 30px; left: 0px; width: 186px;"></div></div></td><td>
<input class="button-link-large buttonBackground" type="submit" value="Buscar">
</td><td><div class="showHelpOuter button-link buttonBackground hideOnMobile" onmouseover="if(typeof showHelp=='function') { showHelp(true); }" onmouseout="if(typeof showHelp=='function') { showHelp(false);} ">?<div id="showHelpInner" class="showHelpInner"></div></div><input type="hidden" name="sL" value="spanish">
<input type="hidden" name="lP" value="spanish-spanish">

</td></tr></tbody></table></form></div><script language="javascript" type="text/javascript" src="/js/functions/verbJS-5.js">

</script>
<div class="specificTenseWrapper">
<div class="specificTenseTable">
<span class="specificTenseHead">Conjuge el verbo activar:</span>
<div class="specificTenseCell"><span class="specificTense" onmouseover="execQuick('/conjugacion/query_spanish.html?conjugation3,activar,activar,_spanish_','present',this);">Presente<span class="specificExcerpt"><br><br>yo activo<br>tú activas<br>...<br><span class="mainsprite showAllElem sprite-yd-show_sp">&nbsp;</span></span></span></div>
<div class="specificTenseCell"><span class="specificTense" onmouseover="execQuick('/conjugacion/query_spanish.html?conjugation3,activar,activar,_spanish_','past',this);">Pasado<span class="specificExcerpt"><br><br>...él ha activado...<br>...nosotros activamos...<br>...vosotros activabais...<br><span class="mainsprite showAllElem sprite-yd-show_sp">&nbsp;</span></span></span></div>
<div class="specificTenseCell"><span class="specificTense" onmouseover="execQuick('/conjugacion/query_spanish.html?conjugation3,activar,activar,_spanish_','future',this);">Futuro<span class="specificExcerpt"><br><br>activarás<br>...<br><br><span class="mainsprite showAllElem sprite-yd-show_sp">&nbsp;</span></span></span></div>
<div class="specificTenseCell"><span class="specificTense" onmouseover="execQuick('/conjugacion/query_spanish.html?conjugation3,activar,activar,_spanish_','conditional',this);">Condicional<span class="specificExcerpt"><br><br>activarías<br>...<br><br><span class="mainsprite showAllElem sprite-yd-show_sp">&nbsp;</span></span></span></div>
<div class="specificTenseCell"><span class="specificTense" onmouseover="execQuick('/conjugacion/query_spanish.html?conjugation3,activar,activar,_spanish_','extra',this);">Subjuntivo<span class="specificExcerpt"><br><br>...<br><br><br><span class="mainsprite showAllElem sprite-yd-show_sp">&nbsp;</span></span></span></div>
<div class="specificTenseCell"><span class="specificTense" id="excerptEmpty"><br><br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="mainsprite sprite-yd-u-sound1" onclick="return openSound('presente', 'activar', 'activar')">&nbsp;</span></span></div>
<div class="clearer"></div>
</div>
</div>
</div><div class="drillBox2">
<form name="conjDrillForm" style="display:inline;" action="/online/servlet/eTranslator.MainServlet" method="post"><input type="hidden" name="eventName" value="directConjLesson"><input type="hidden" name="lang" value="2"><input type="hidden" name="sourceLanguage" id="sourceLanguage" value="extra"><input type="hidden" name="targetLanguage" id="targetLanguage" value="spanish"><input type="hidden" name="verb_infinitiv" value="activar"><div style="float:left;width:180px;padding-right:20px;">Ejercicios de 'activar'</div><div style="overflow:hidden;text-align:right;"><input class="button-link-large buttonBackground" style="" type="submit" value="Start"></div><div class="clearer"></div><div style="padding:15px 0px 0px 5px;font-size:10px;text-align:center;"><input checked="" type="checkbox" name="timeForms" value="GENERAL_PRESENT">Presente&nbsp;&nbsp; <input type="checkbox" name="timeForms" value="GENERAL_PAST">Pasado&nbsp;&nbsp; <input checked="" type="checkbox" name="timeForms" value="GENERAL_FUTURE">Futuro</div></form>
</div>
<div class="clearer"></div></div><div class="nextVerbs2">
<b>Los próximos verbos en español en nuestra lista: </b><br>
<a class="nextWords" href="/conjugacion3/actualizar.html">actualizar</a>&nbsp;&nbsp;  <a class="nextWords" href="/conjugacion2/actuar.html">actuar</a>&nbsp;&nbsp;  <a class="nextWords" href="/conjugacion3/acuartelar.html">acuartelar</a>&nbsp;&nbsp;  <a class="nextWords" href="/conjugacion3/acudir.html">acudir</a>&nbsp;&nbsp;  <a class="nextWords" href="/conjugacion2/acumular.html">acumular</a>&nbsp;&nbsp;  <a class="nextWords" href="/conjugacion3/acunar.html">acunar</a>&nbsp;&nbsp;  
</div>
<div id="newsletterHolder" class="newsletter2"></div>
<div class="clearer"></div><div class="belowMainBoxDiv" id="belowMainBoxDiv"></div><div class="alphabetIndex">
<script language="javascript" type="text/javascript">
<!--

getLinkToMenu(new Array("a","a1","a2","b","c","c1","d","d1","e","e1","f","g","h","i","j","k","l","m","n","o","p","p1","q","r","r1","s","t","u","v","w","x","y","z"),'spanish','spanish');
// -->

</script><a class="x" href="../conjugacion2/a_spanish.html">a</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/a1_spanish.html">a1</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/a2_spanish.html">a2</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/b_spanish.html">b</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/c_spanish.html">c</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/c1_spanish.html">c1</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/d_spanish.html">d</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/d1_spanish.html">d1</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/e_spanish.html">e</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/e1_spanish.html">e1</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/f_spanish.html">f</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/g_spanish.html">g</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/h_spanish.html">h</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/i_spanish.html">i</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/j_spanish.html">j</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/k_spanish.html">k</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/l_spanish.html">l</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/m_spanish.html">m</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/n_spanish.html">n</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/o_spanish.html">o</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/p_spanish.html">p</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/p1_spanish.html">p1</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/q_spanish.html">q</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/r_spanish.html">r</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/r1_spanish.html">r1</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/s_spanish.html">s</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/t_spanish.html">t</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/u_spanish.html">u</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/v_spanish.html">v</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/w_spanish.html">w</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/x_spanish.html">x</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/y_spanish.html">y</a>&nbsp;&nbsp; <a class="x" href="../conjugacion2/z_spanish.html">z</a>&nbsp;&nbsp; 
</div><br>
<div class="lowerPaneDiv" id="lowerPaneDiv"></div><div id="conjSkyAdWrapperID" class="conjSkyAdWrapper" style="top: 25px;"><!--start skyscraper/logo panel--><!-- Conjugation Asynch 160x600 -->
<ins class="adsbygoogle conjSkyResponsive" data-ad-client="ca-pub-3415784549533464" data-ad-slot="1418040737" data-adsbygoogle-status="done" style="width: 160px; height: 600px;" data-ad-status="filled"><div id="aswift_1_host" style="border: none; height: 600px; width: 160px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: inline-block;"><iframe id="aswift_1" name="aswift_1" style="left:0;position:absolute;top:0;border:0;width:160px;height:600px;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="160" height="600" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allow="attribution-reporting; run-ad-auction" src="https://pagead2.googlesyndication.com/pagead/ads?ltd_cs=1&amp;client=ca-pub-3415784549533464&amp;output=html&amp;h=600&amp;slotname=1418040737&amp;adk=3848974873&amp;adf=3128849423&amp;pi=t.ma~as.1418040737&amp;w=160&amp;abgtt=3&amp;lmt=1711871510&amp;rafmt=12&amp;format=160x600&amp;url=https%3A%2F%2Fwww.vocabulix.com%2Fconjugacion3%2Factivar.html&amp;wgl=1&amp;uach=WyJtYWNPUyIsIjEyLjcuMiIsIng4NiIsIiIsIjEyMy4wLjYzMTIuODciLG51bGwsMCxudWxsLCI2NCIsW1siR29vZ2xlIENocm9tZSIsIjEyMy4wLjYzMTIuODciXSxbIk5vdDpBLUJyYW5kIiwiOC4wLjAuMCJdLFsiQ2hyb21pdW0iLCIxMjMuMC42MzEyLjg3Il1dLDBd&amp;dt=1711875570112&amp;bpp=1&amp;bdt=180&amp;idt=27&amp;shv=r20240327&amp;mjsv=m202403250101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;eo_id_str=ID%3Dbb8f32e6ab7cfb3f%3AT%3D1711870727%3ART%3D1711875539%3AS%3DAA-AfjbnZc70O3pI3j4Vx3TFgXqN&amp;prev_fmts=300x250&amp;correlator=6372637868985&amp;frm=20&amp;pv=1&amp;ga_vid=347672392.1711875570&amp;ga_sid=1711875570&amp;ga_hid=1893198956&amp;ga_fc=0&amp;u_tz=120&amp;u_his=20&amp;u_h=900&amp;u_w=1440&amp;u_ah=875&amp;u_aw=1440&amp;u_cd=24&amp;u_sd=2&amp;dmc=8&amp;adx=131&amp;ady=218&amp;biw=1440&amp;bih=754&amp;scr_x=0&amp;scr_y=0&amp;eid=44759875%2C44759926%2C44759842%2C31081576%2C31082197%2C44795921%2C95326315%2C95329017%2C95322183%2C95328825%2C31078663%2C31078665%2C31078668%2C31078670&amp;oid=2&amp;pvsid=4425896326566574&amp;tmod=667825585&amp;uas=0&amp;nvt=1&amp;ref=https%3A%2F%2Fwww.vocabulix.com%2Fconjugacion2%2Fa_spanish.html&amp;fc=640&amp;brdim=0%2C25%2C0%2C25%2C1440%2C25%2C1440%2C875%2C1440%2C754&amp;vis=1&amp;rsz=%7C%7CaE%7C&amp;abl=CA&amp;pfx=0&amp;fu=256&amp;bc=31&amp;bz=1&amp;td=1&amp;nt=1&amp;ifi=2&amp;uci=a!2&amp;fsb=1&amp;dtd=29" data-google-container-id="a!2" tabindex="0" title="Advertisement" aria-label="Advertisement" data-google-query-id="CPT6kbqRnoUDFZmCdwEdGa8EqQ" data-load-complete="true"></iframe></div></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div><!--end skyscraper/logo panel--><script language="javascript" type="text/javascript">

<!--

INF_JS='activar';
INF_HTML='activar';
FILE_NAME='activar';
displayWelcome();

// -->

</script>

<noscript><img width="330" height="18" alt='' src='../images/javascript_spanish.png'></noscript>
<br><br><div class="conjLargeBox"><div class="conjLargeBoxLeft">
<script type="text/javascript" language="javascript" src="../js/rev_conjugation3/Y_activar.js"></script>
<div class="conjBlock">
<span class="sprite-spanish sprite-GENERAL_PRESENT_spanish"></span><br><br>
<span class="sprite-spanish sprite-1_spanish"></span>
activo
<br>
<span class="sprite-spanish sprite-2_spanish"></span>
activas
<br>
<span class="sprite-spanish sprite-3_spanish"></span>
activa
<br>
<span class="sprite-spanish sprite-4_spanish"></span>
activamos
<br>
<span class="sprite-spanish sprite-5_spanish"></span>
activáis
<br>
<span class="sprite-spanish sprite-6_spanish"></span>
activan
<br>

</div>
<div class="conjBlock">
<span class="sprite-spanish sprite-GENERAL_PERFECT_spanish"></span><br><br>
<script language="javascript" type="text/javascript"><!--
document.write(conjugate_activar('Pret\u00e9rito perfecto compuesto'));

// -->
</script>yo he activado<br>tú has activado<br>él ha activado<br>nosotros hemos activado<br>vosotros habéis activado<br>ellos han activado<br>
</div>
<div class="conjBlock">
<span class="sprite-spanish sprite-GENERAL_PAST_2_spanish"></span><br><br>
<span class="sprite-spanish sprite-1_spanish"></span>
activaba
<br>
<span class="sprite-spanish sprite-2_spanish"></span>
activabas
<br>
<span class="sprite-spanish sprite-3_spanish"></span>
activaba
<br>
<span class="sprite-spanish sprite-4_spanish"></span>
activábamos
<br>
<span class="sprite-spanish sprite-5_spanish"></span>
activabais
<br>
<span class="sprite-spanish sprite-6_spanish"></span>
activaban
<br>

</div>
<div class="conjBlock">
<script language="javascript" type="text/javascript"><!--
document.write('<b>Pret&#233;rito pluscuamperfecto<\/b><br><br>');

// -->
</script><b>Pretérito pluscuamperfecto</b><br><br>
<script language="javascript" type="text/javascript"><!--
document.write(conjugate_activar('Pret\u00e9rito pluscuamperfecto'));

// -->
</script>yo había activado<br>tú habías activado<br>él había activado<br>nosotros habíamos activado<br>vosotros habíais activado<br>ellos habían activado<br>
</div>
<div class="conjBlock">
<span class="sprite-spanish sprite-GENERAL_PAST_spanish"></span><br><br>
<span class="sprite-spanish sprite-1_spanish"></span>
activé
<br>
<span class="sprite-spanish sprite-2_spanish"></span>
activaste
<br>
<span class="sprite-spanish sprite-3_spanish"></span>
activó
<br>
<span class="sprite-spanish sprite-4_spanish"></span>
activamos
<br>
<span class="sprite-spanish sprite-5_spanish"></span>
activasteis
<br>
<span class="sprite-spanish sprite-6_spanish"></span>
activaron
<br>

</div>
<div class="conjBlock">
<script language="javascript" type="text/javascript"><!--
document.write('<b>Pret&#233;rito anterior<\/b><br><br>');

// -->
</script><b>Pretérito anterior</b><br><br>
<script language="javascript" type="text/javascript"><!--
document.write(conjugate_activar('Pret\u00e9rito anterior'));

// -->
</script>yo hube activado<br>tú hubiste activado<br>él hubo activado<br>nosotros hubimos activado<br>vosotros hubisteis activado<br>ellos hubieron activado<br>
</div>
<div class="conjBlockAd" style="margin: 0px; padding: 0px; border-width: 0px;">
<!-- ConjResponsiveLower -->
<ins class="adsbygoogle conjLowerResponsive" data-ad-client="ca-pub-3415784549533464" data-ad-slot="9672204730" data-adsbygoogle-status="done" style="width: 0px; height: 0px;" data-ad-status="unfilled"><div id="aswift_2_host" style="border: none; height: 0px; width: 0px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: inline-block; overflow: hidden; opacity: 0;"><iframe id="aswift_2" name="aswift_2" style="left: 0px; position: absolute; top: 0px; border: 0px; width: 0px; height: 0px;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="0" height="0" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allow="attribution-reporting; run-ad-auction" src="https://pagead2.googlesyndication.com/pagead/ads?ltd_cs=1&amp;client=ca-pub-3415784549533464&amp;output=html&amp;h=250&amp;slotname=9672204730&amp;adk=189335732&amp;adf=3527530770&amp;pi=t.ma~as.9672204730&amp;w=300&amp;abgtt=3&amp;lmt=1711871510&amp;rafmt=12&amp;format=300x250&amp;url=https%3A%2F%2Fwww.vocabulix.com%2Fconjugacion3%2Factivar.html&amp;wgl=1&amp;uach=WyJtYWNPUyIsIjEyLjcuMiIsIng4NiIsIiIsIjEyMy4wLjYzMTIuODciLG51bGwsMCxudWxsLCI2NCIsW1siR29vZ2xlIENocm9tZSIsIjEyMy4wLjYzMTIuODciXSxbIk5vdDpBLUJyYW5kIiwiOC4wLjAuMCJdLFsiQ2hyb21pdW0iLCIxMjMuMC42MzEyLjg3Il1dLDBd&amp;dt=1711875570180&amp;bpp=2&amp;bdt=249&amp;idt=2&amp;shv=r20240327&amp;mjsv=m202403250101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;eo_id_str=ID%3Dbb8f32e6ab7cfb3f%3AT%3D1711870727%3ART%3D1711875539%3AS%3DAA-AfjbnZc70O3pI3j4Vx3TFgXqN&amp;prev_fmts=300x250%2C160x600&amp;correlator=6372637868985&amp;frm=20&amp;pv=1&amp;ga_vid=347672392.1711875570&amp;ga_sid=1711875570&amp;ga_hid=1893198956&amp;ga_fc=0&amp;u_tz=120&amp;u_his=20&amp;u_h=900&amp;u_w=1440&amp;u_ah=875&amp;u_aw=1440&amp;u_cd=24&amp;u_sd=2&amp;dmc=8&amp;adx=332&amp;ady=1190&amp;biw=1440&amp;bih=754&amp;scr_x=0&amp;scr_y=0&amp;eid=44759875%2C44759926%2C44759842%2C31081576%2C31082197%2C44795921%2C95326315%2C95329017%2C95322183%2C95328825%2C31078663%2C31078665%2C31078668%2C31078670&amp;oid=2&amp;pvsid=4425896326566574&amp;tmod=667825585&amp;uas=0&amp;nvt=1&amp;ref=https%3A%2F%2Fwww.vocabulix.com%2Fconjugacion2%2Fa_spanish.html&amp;fc=640&amp;brdim=0%2C25%2C0%2C25%2C1440%2C25%2C1440%2C875%2C1440%2C754&amp;vis=1&amp;rsz=%7C%7CleEbr%7C&amp;abl=CS&amp;pfx=0&amp;fu=256&amp;bc=31&amp;bz=1&amp;td=1&amp;nt=1&amp;ifi=3&amp;uci=a!3&amp;btvi=1&amp;fsb=1&amp;dtd=4" data-google-container-id="a!3" tabindex="0" title="Advertisement" aria-label="Advertisement" data-google-query-id="CMLZlLqRnoUDFXuN0QQdK1kPEQ" data-load-complete="true"></iframe></div></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>
<div class="conjBlock">
<span class="sprite-spanish sprite-GENERAL_FUTURE_spanish"></span><br><br>
<span class="sprite-spanish sprite-1_spanish"></span>
activaré
<br>
<span class="sprite-spanish sprite-2_spanish"></span>
activarás
<br>
<span class="sprite-spanish sprite-3_spanish"></span>
activará
<br>
<span class="sprite-spanish sprite-4_spanish"></span>
activaremos
<br>
<span class="sprite-spanish sprite-5_spanish"></span>
activaréis
<br>
<span class="sprite-spanish sprite-6_spanish"></span>
activarán
<br>

</div>
<div class="conjBlock">
<script language="javascript" type="text/javascript"><!--
document.write('<b>Futuro perfecto<\/b><br><br>');

// -->
</script><b>Futuro perfecto</b><br><br>
<script language="javascript" type="text/javascript"><!--
document.write(conjugate_activar('Futuro perfecto'));

// -->
</script>yo habré activado<br>tú habrás activado<br>él habrá activado<br>nosotros habremos activado<br>vosotros habréis activado<br>ellos habrán activado<br>
</div>
<div class="conjBlock">
<script language="javascript" type="text/javascript"><!--
document.write('<b>Presente Subjuntivo<\/b><br><br>');

// -->
</script><b>Presente Subjuntivo</b><br><br>
<script language="javascript" type="text/javascript"><!--
document.write(conjugate_activar('Presente Subjuntivo'));

// -->
</script>yo active<br>tú actives<br>él active<br>nosotros activemos<br>vosotros activéis<br>ellos activen<br>
</div>
<div class="conjBlock">
<script language="javascript" type="text/javascript"><!--
document.write('<b>Pret&#233;rito perfecto Subjuntivo<\/b><br><br>');

// -->
</script><b>Pretérito perfecto Subjuntivo</b><br><br>
<script language="javascript" type="text/javascript"><!--
document.write(conjugate_activar('Pret\u00e9rito perfecto Subjuntivo'));

// -->
</script>yo haya activado<br>tú hayas activado<br>él haya activado<br>nosotros hayamos activado<br>vosotros hayáis activado<br>ellos hayan activado<br>
</div>
<div class="conjBlock">
<script language="javascript" type="text/javascript"><!--
document.write('<b>Futuro Subjuntivo<\/b><br><br>');

// -->
</script><b>Futuro Subjuntivo</b><br><br>
<script language="javascript" type="text/javascript"><!--
document.write(conjugate_activar('Futuro Subjuntivo'));

// -->
</script>yo activare<br>tú activares<br>él activare<br>nosotros activáremos<br>vosotros activareis<br>ellos activaren<br>
</div>
<div class="conjBlock">
<script language="javascript" type="text/javascript"><!--
document.write('<b>Futuro perfecto Subjuntivo<\/b><br><br>');

// -->
</script><b>Futuro perfecto Subjuntivo</b><br><br>
<script language="javascript" type="text/javascript"><!--
document.write(conjugate_activar('Futuro perfecto Subjuntivo'));

// -->
</script>yo hubiere activado<br>tú hubieres activado<br>él hubiere activado<br>nosotros hubiéremos activado<br>vosotros hubiereis activado<br>ellos hubieren activado<br>
</div>
<div class="conjBlock">
<span class="sprite-spanish sprite-GENERAL_CONDITIONAL_spanish"></span><br><br>
<span class="sprite-spanish sprite-1_spanish"></span>
activaría
<br>
<span class="sprite-spanish sprite-2_spanish"></span>
activarías
<br>
<span class="sprite-spanish sprite-3_spanish"></span>
activaría
<br>
<span class="sprite-spanish sprite-4_spanish"></span>
activaríamos
<br>
<span class="sprite-spanish sprite-5_spanish"></span>
activaríais
<br>
<span class="sprite-spanish sprite-6_spanish"></span>
activarían
<br>

</div>
<div class="conjBlock">
<script language="javascript" type="text/javascript"><!--
document.write('<b>Condicional compuesto<\/b><br><br>');

// -->
</script><b>Condicional compuesto</b><br><br>
<script language="javascript" type="text/javascript"><!--
document.write(conjugate_activar('Condicional compuesto'));

// -->
</script>yo habría activado<br>tú habrías activado<br>él habría activado<br>nosotros habríamos activado<br>vosotros habríais activado<br>ellos habrían activado<br>
</div>
<div class="clearer"></div>
</div><div class="conjLargeBoxRight">
<!-- 160x90, lower side menu Asynch -->
<ins class="adsbygoogle" style="display: inline-block; width: 160px; height: 0px;" data-ad-slot="2459122336" data-ad-client="ca-pub-3415784549533464" data-adsbygoogle-status="done" data-ad-status="unfilled"><div id="aswift_3_host" style="border: none; height: 0px; width: 160px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: inline-block; overflow: hidden; opacity: 0;"><iframe id="aswift_3" name="aswift_3" style="left: 0px; position: absolute; top: 0px; border: 0px; width: 160px; height: 0px;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="160" height="0" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allow="attribution-reporting; run-ad-auction" src="https://pagead2.googlesyndication.com/pagead/ads?ltd_cs=1&amp;client=ca-pub-3415784549533464&amp;output=html&amp;h=90&amp;slotname=2459122336&amp;adk=209452861&amp;adf=3145053412&amp;pi=t.ma~as.2459122336&amp;w=160&amp;abgtt=3&amp;lmt=1711871510&amp;url=https%3A%2F%2Fwww.vocabulix.com%2Fconjugacion3%2Factivar.html&amp;wgl=1&amp;uach=WyJtYWNPUyIsIjEyLjcuMiIsIng4NiIsIiIsIjEyMy4wLjYzMTIuODciLG51bGwsMCxudWxsLCI2NCIsW1siR29vZ2xlIENocm9tZSIsIjEyMy4wLjYzMTIuODciXSxbIk5vdDpBLUJyYW5kIiwiOC4wLjAuMCJdLFsiQ2hyb21pdW0iLCIxMjMuMC42MzEyLjg3Il1dLDBd&amp;dt=1711875570193&amp;bpp=1&amp;bdt=261&amp;idt=1&amp;shv=r20240327&amp;mjsv=m202403250101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;eo_id_str=ID%3Dbb8f32e6ab7cfb3f%3AT%3D1711870727%3ART%3D1711875539%3AS%3DAA-AfjbnZc70O3pI3j4Vx3TFgXqN&amp;prev_fmts=300x250%2C160x600%2C300x250&amp;correlator=6372637868985&amp;frm=20&amp;pv=1&amp;ga_vid=347672392.1711875570&amp;ga_sid=1711875570&amp;ga_hid=1893198956&amp;ga_fc=0&amp;u_tz=120&amp;u_his=20&amp;u_h=900&amp;u_w=1440&amp;u_ah=875&amp;u_aw=1440&amp;u_cd=24&amp;u_sd=2&amp;dmc=8&amp;adx=327&amp;ady=1861&amp;biw=1440&amp;bih=754&amp;scr_x=0&amp;scr_y=0&amp;eid=44759875%2C44759926%2C44759842%2C31081576%2C31082197%2C44795921%2C95326315%2C95329017%2C95322183%2C95328825%2C31078663%2C31078665%2C31078668%2C31078670&amp;oid=2&amp;pvsid=4425896326566574&amp;tmod=667825585&amp;uas=0&amp;nvt=1&amp;ref=https%3A%2F%2Fwww.vocabulix.com%2Fconjugacion2%2Fa_spanish.html&amp;fc=640&amp;brdim=0%2C25%2C0%2C25%2C1440%2C25%2C1440%2C875%2C1440%2C754&amp;vis=1&amp;rsz=%7C%7CeEbr%7C&amp;abl=CS&amp;pfx=0&amp;fu=0&amp;bc=31&amp;bz=1&amp;td=1&amp;nt=1&amp;ifi=4&amp;uci=a!4&amp;btvi=2&amp;fsb=1&amp;dtd=3" data-google-container-id="a!4" tabindex="0" title="Advertisement" aria-label="Advertisement" data-google-query-id="CLXQlbqRnoUDFeC90QQdOWUMjg" data-load-complete="true"></iframe></div></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div><div class="clearer"></div></div><br>
<div class="tableWrapperMReadyHorizontal">
<br><br><table id="forumBlock" class="forum"><tbody><tr><td class="forum"><img id="forumImg" width="190" height="80" src="//static.vocabulix.com/images/dict/dic_ad_spanish.png"></td><td><div class="forum">Subimos al barco y dejamos el puerto. Comenzamos con un almuerzo que estuvo bastante bien. El barco navegó durante aproximadamente una hora hasta llegar a la zona de la bahía, que tiene más de mil islas.<br>Fuimos a visitar los distintos mercados, comenzando por el mercado de pulseras de Kowloon. Lili compró algunas piedras allí. Por la tarde visitamos el distrito financiero, al que sólo se podía llegar en bote.<br>HOLA es Español y significa HI, ¿no es cierto? ¿Cómo es la vida en Brasil? ¿Es realmente tan peligroso como dicen en la televisión? ¡Quizás me puedan contar un poco de tu país, en Español, así yo puedo corregir tus oraciones!</div></td></tr></tbody></table><br></div>
</div><div id="lastPanelId"></div><!-- end mainpanel --></div><div class="clearer"></div></div>
<ins class="adsbygoogle adsbygoogle-noablate" data-adsbygoogle-status="done" style="display: none !important;" data-ad-status="unfilled"><div id="aswift_4_host" style="border: none; height: 0px; width: 0px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: inline-block;"><iframe id="aswift_4" name="aswift_4" style="left:0;position:absolute;top:0;border:0;width:undefinedpx;height:undefinedpx;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allow="attribution-reporting; run-ad-auction" src="https://pagead2.googlesyndication.com/pagead/ads?ltd_cs=1&amp;client=ca-pub-3415784549533464&amp;output=html&amp;adk=1812271804&amp;adf=3025194257&amp;abgtt=3&amp;lmt=1711871510&amp;plat=2%3A16777216%2C8%3A4194304%2C9%3A134250504%2C16%3A8388608%2C17%3A32%2C24%3A32%2C25%3A32%2C30%3A1081344%2C32%3A32%2C41%3A32%2C42%3A32&amp;plas=128x595_l%7C279x595_r&amp;format=0x0&amp;url=https%3A%2F%2Fwww.vocabulix.com%2Fconjugacion3%2Factivar.html&amp;pra=7&amp;wgl=1&amp;easpi=0&amp;asro=0&amp;uach=WyJtYWNPUyIsIjEyLjcuMiIsIng4NiIsIiIsIjEyMy4wLjYzMTIuODciLG51bGwsMCxudWxsLCI2NCIsW1siR29vZ2xlIENocm9tZSIsIjEyMy4wLjYzMTIuODciXSxbIk5vdDpBLUJyYW5kIiwiOC4wLjAuMCJdLFsiQ2hyb21pdW0iLCIxMjMuMC42MzEyLjg3Il1dLDBd&amp;dt=1711875570201&amp;bpp=1&amp;bdt=269&amp;idt=1&amp;shv=r20240327&amp;mjsv=m202403250101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;eo_id_str=ID%3Dbb8f32e6ab7cfb3f%3AT%3D1711870727%3ART%3D1711875539%3AS%3DAA-AfjbnZc70O3pI3j4Vx3TFgXqN&amp;prev_fmts=300x250%2C160x600%2C300x250&amp;prev_slotnames=2459122336&amp;nras=1&amp;correlator=6372637868985&amp;frm=20&amp;pv=1&amp;ga_vid=347672392.1711875570&amp;ga_sid=1711875570&amp;ga_hid=1893198956&amp;ga_fc=0&amp;u_tz=120&amp;u_his=20&amp;u_h=900&amp;u_w=1440&amp;u_ah=875&amp;u_aw=1440&amp;u_cd=24&amp;u_sd=2&amp;dmc=8&amp;adx=-12245933&amp;ady=-12245933&amp;biw=1440&amp;bih=754&amp;scr_x=0&amp;scr_y=0&amp;eid=44759875%2C44759926%2C44759842%2C31081576%2C31082197%2C44795921%2C95326315%2C95329017%2C95322183%2C95328825%2C31078663%2C31078665%2C31078668%2C31078670&amp;oid=2&amp;pvsid=4425896326566574&amp;tmod=667825585&amp;uas=0&amp;nvt=1&amp;fsapi=1&amp;ref=https%3A%2F%2Fwww.vocabulix.com%2Fconjugacion2%2Fa_spanish.html&amp;fc=896&amp;brdim=0%2C25%2C0%2C25%2C1440%2C25%2C1440%2C875%2C1440%2C754&amp;vis=1&amp;rsz=%7C%7Cs%7C&amp;abl=NS&amp;fu=32768&amp;bc=31&amp;bz=1&amp;td=1&amp;nt=1&amp;ifi=5&amp;uci=a!5&amp;fsb=1&amp;dtd=11" data-google-container-id="a!5" tabindex="0" title="Advertisement" aria-label="Advertisement" data-load-complete="true"></iframe></div></ins><div id="loom-companion-mv3" ext-id="liecbddmkiiihnedobmlmillhodjkdmb"><section id="shadow-host-companion"></section></div><ins class="adsbygoogle adsbygoogle-noablate" data-adsbygoogle-status="done" data-anchor-status="dismissed" data-ad-status="filled" style="display: none; width: 100% !important; height: 129px !important; bottom: -124px; clear: none !important; float: none !important; left: 0px; margin: 0px !important; max-height: none !important; max-width: none !important; opacity: 1; overflow: visible !important; padding: 0px !important; position: fixed; right: auto !important; top: auto !important; vertical-align: baseline !important; visibility: visible !important; z-index: 2147483647; background: rgb(250, 250, 250) !important;" data-anchor-shown="true"><div class="grippy-host"></div><div id="aswift_5_host" style="border: none !important; height: 124px !important; width: 100% !important; margin: 0px !important; padding: 0px !important; position: relative !important; visibility: visible !important; background-color: transparent !important; display: inline-block !important; inset: auto !important; clear: none !important; float: none !important; max-height: none !important; max-width: none !important; opacity: 1 !important; overflow: visible !important; vertical-align: baseline !important; z-index: auto !important;"><iframe id="aswift_5" name="aswift_5" style="width: 1005px !important; height: 124px !important; display: block; margin: 0px auto;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="1005" height="124" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allow="attribution-reporting; run-ad-auction" src="https://pagead2.googlesyndication.com/pagead/html/r20240327/r20110914/zrt_lookup_fy2021.html#RS-0-&amp;adk=1812271801&amp;client=ca-pub-3415784549533464&amp;fa=1&amp;ifi=6&amp;uci=a!6&amp;btvi=3" data-google-container-id="a!6" tabindex="0" title="Advertisement" aria-label="Advertisement" data-google-query-id="CNvolrqRnoUDFQui0QQdoaEPhA" data-load-complete="true"></iframe></div></ins></body></html>'''  # Reemplaza esto con tu HTML


# Importamos Excel con las URLs
archivo_excel = '/Users/aitor/Desktop/conjugaciones_verbales/archivos_datos/archivos_para_importar/listado_urls_para_scraping_conjugaciones.xlsx'
df = pd.read_excel(archivo_excel)
print(df)

# Función para extraer las conjugaciones de una página web
def extraer_conjugaciones(url):
    response = requests.get(url)
    conjugations = set()
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        conj_blocks = soup.find_all('div', class_='conjBlock')
        prefixes = ("yo ", "tu ", "tú ", "él ", "el ", "nosotros ", "vosotros ", "ellos ")

        for block in conj_blocks:
            for child in block.children:
                if isinstance(child, NavigableString):
                    text = child.strip()
                    if text:
                        for prefix in prefixes:
                            if text.startswith(prefix):
                                text = text[len(prefix):]
                                break
                        conjugations.add(text)
                elif child.name == 'br':
                    next_sib = child.nextSibling
                    if next_sib and isinstance(next_sib, NavigableString):
                        text = next_sib.strip()
                        if text:
                            for prefix in prefixes:
                                if text.startswith(prefix):
                                    text = text[len(prefix):]
                                    break
                            conjugations.add(text)
    else:
        print('Error al obtener la página:', response.status_code)

    return sorted(conjugations)  # Devolver conjugaciones ordenadas

# Lista para almacenar todas las conjugaciones
todas_conjugaciones = []

# Iterar sobre cada URL en el DataFrame
for index, row in df.iterrows():
    url = row['url_completa']
    conjugaciones = extraer_conjugaciones(url)
    todas_conjugaciones.extend(conjugaciones)  # Agregar conjugaciones a la lista

# Convertir la lista de conjugaciones a un DataFrame
resultados_conjugaciones_df = pd.DataFrame(todas_conjugaciones, columns=['Conjugaciones'])

# Guardar los resultados en un archivo Excel
ruta_excel = '/Users/aitor/Desktop/conjugaciones_verbales/archivos_datos/archivos_exportados/resultados_conjugaciones.xlsx'
resultados_conjugaciones_df.to_excel(ruta_excel, index=False)

print(f'Archivo guardado en {ruta_excel}')












'''# Parseamos el HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Encuentra todos los bloques que contienen las conjugaciones
conj_blocks = soup.find_all('div', class_='conjBlock')

# Conjunto para almacenar todas las conjugaciones únicas
conjugations = set()

# Cadenas para eliminar del inicio de cada conjugación
prefixes = ("yo ", "tu ", "tú ", "él ", "el ", "nosotros ", "vosotros ", "ellos ")

for block in conj_blocks:
    for child in block.children:
        if isinstance(child, NavigableString):
            text = child.strip()
            if text:
                # Eliminar los prefijos especificados
                for prefix in prefixes:
                    if text.startswith(prefix):
                        text = text[len(prefix):]
                        break
                conjugations.add(text)
        elif child.name == 'br':
            next_sib = child.nextSibling
            if next_sib and isinstance(next_sib, NavigableString):
                text = next_sib.strip()
                if text:
                    # Eliminar los prefijos especificados
                    for prefix in prefixes:
                        if text.startswith(prefix):
                            text = text[len(prefix):]
                            break
                    conjugations.add(text)

# Convertir el conjunto a lista para operaciones futuras, si es necesario
conjugations_list = list(conjugations)

# Imprime todas las conjugaciones únicas encontradas
for conjugation in sorted(conjugations_list):  # sorted para imprimir de manera ordenada
    print(conjugation)
'''