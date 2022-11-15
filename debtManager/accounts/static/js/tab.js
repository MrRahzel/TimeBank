var tabCount = 3;
function SelectTab(idx) {
	for (var i = 1; i <= tabCount; ++i)
		{
			var _tab = document.getElementById("tab"+i);
			var _tabTitle = document.getElementById("tab-title"+i);
			if (idx != i) {
				_tab.setAttribute("class", "tab");
				_tabTitle.setAttribute("class", "tab-title");
				}
			else {
				_tab.setAttribute("class", "tab selected");
				_tabTitle.setAttribute("class", "tab-title selected-li");
				}
		}
	}
