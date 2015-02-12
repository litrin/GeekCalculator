import sublime_plugin
import time

class GeekCalculatorCommand(sublime_plugin.TextCommand):
	
	Separator = "\n" 

	def run(self, edit):
		selected_regions = self.view.sel()
		for region in selected_regions:
			selected = self.view.substr( region );
      if re.match('^[0-9+\-*/%\(\). ]+$', expr):
        result = eval( expr )
			self.view.replace( edit, region, str( result ) )

    def calculate(self, selected):
    	selected = selected.split(self.Separator)
    	result = list()
    	for expr in selected:
    		try:
    			formula = "%s=%s" % (expr, eval(expr))
    		except:
    			formula = expr
    		result.append(formula)

    	return self.Separator.join(result)


