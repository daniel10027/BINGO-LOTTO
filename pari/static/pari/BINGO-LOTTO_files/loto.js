
function Loto_Write(szValue)
{
	document.write("<a title=\"R&eacute;sultats Loto fournis par Les Secrets du Jeu : stats, syst&egrave;mes, logiciels Loto gratuits...\" class=Loto target=_blank href=https://www.secretsdujeu.com/page/jeux_loto_resultats.html>" + szValue + "</a>");
}

function Loto_GetDate()
{
	Loto_Write("<span class=LotoDate>Samedi<br>27 Juillet</span>");
}

function Loto_GetShortDate()
{
	Loto_Write("<span class=LotoDate>27 Juillet 2019</span>");
}

function Loto_GetNumero(iTirage, iNumero)
{
	var tirage = new Array(3);
	tirage[1] = new Array(8);


	tirage[1][1] = 25;

	tirage[1][2] = 28;

	tirage[1][3] = 31;

	tirage[1][4] = 39;

	tirage[1][5] = 47;

	tirage[1][6] = 8;


	Loto_Write("<span class=LotoNumero>" + tirage[iTirage][iNumero] + "</span>");
}

function Loto_GetJocker()
{
	Loto_Write("<span class=LotoJocker>7 140 557</span>");
}

function Loto_ShowResultats()
{
	document.write("<table class=LotoTable>");
	document.write("<tr>");
	document.write("<td>");
	document.write("<table border=0 cellspacing=0 cellpadding=1>");
	document.write("<tr>");
	document.write("<td align=center colspan=10>");
	document.write("<span class=LotoTitle>LOTO</span>");
	document.write("</td>");
	document.write("</tr>");
	document.write("<tr>");
	document.write("<td align=center width=100% colspan=10>");
	document.write("<table width=100% border=0 cellspacing=0 cellpadding=0>");
	document.write("<tr>");
	document.write("<td align=right>");Loto_Write("<img border=\"0\" width=\"10\" height=\"18\" src=\"https://secretsdujeu.com/media/4Fw5SAm\">");document.write("</a></td>");
	document.write("<td align=center>");Loto_GetDate();document.write("</td>");
	document.write("<td align=left>");Loto_Write("<img border=\"0\" width=\"10\" height=\"18\" src=\"https://secretsdujeu.com/media/lyaSqPZ\">");document.write("</a></td>");
	document.write("</tr>");
	document.write("</table>");
	document.write("</td>");
	document.write("</tr>");
	document.write("<tr>");
	document.write("<td align=center colspan=10 style='height:10px;line-height:1px;'><img border=0 src=\"https://secretsdujeu.com/media/se9hyVV\" width=150 height=1></td>");
	document.write("</tr>");
	document.write("<tr>");
	document.write("<td align=center style='width:16%;'>");Loto_GetNumero(1,1);document.write("</td>");
	document.write("<td align=center style='width:16%;'>");Loto_GetNumero(1,2);document.write("</td>");
	document.write("<td align=center style='width:16%;'>");Loto_GetNumero(1,3);document.write("</td>");
	document.write("<td align=center style='width:16%;'>");Loto_GetNumero(1,4);document.write("</td>");
	document.write("<td align=center style='width:16%;'>");Loto_GetNumero(1,5);document.write("</td>");
	document.write("<td align=center style='width:4%;'><span class=Loto_Numero>-</span></td>");
	document.write("<td align=center style='width:16%;'>");Loto_GetNumero(1,6);document.write("</td>");
	document.write("</tr>");
	document.write("<tr>");
	document.write("<td align=center colspan=10 style='height:10px;line-height:1px;'><img border=0 src=\"https://secretsdujeu.com/media/se9hyVV\" width=150 height=1></td>");
	document.write("</tr>");
	document.write("<tr>");
	document.write("<td align=center width=100% colspan=10 style='height:26px;'><span class=LotoJocker>Jocker+ : </span>");Loto_GetJocker();document.write("</td>");
	document.write("</tr>");
	document.write("</table>");
	document.write("</td>");
	document.write("</tr>");
	document.write("</table>");
}
