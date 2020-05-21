import typing
class Spec:
	def __init__(self, description:str ="",attribute: typing.Union[str,list] ="",value: typing.Union[str,list]="",
				 filterOp:str ="=", channel:str ="", dataType:str="",dataModel:str="",
				 aggregation:str = "", binSize:int=0, weight:float=1,sort:str=""):
		"""
		Spec is the object representation of a single unit of the specification.

		Parameters
		----------
		description : str, optional
			Convenient shorthand description of specification, parser parses description into other properties (attribute, value, filterOp), by default ""
		attribute : typing.Union[str,list], optional
			Specified attribute(s) of interest, by default ""
			By providing a list of attributes (e.g., [Origin,Brand]), user is interested in either one of the attribute (i.e., Origin or Brand).
		value : typing.Union[str,list], optional
			Specified value(s) of interest, by default ""
			By providing a list of values (e.g., ["USA","Europe"]), user is interested in either one of the attribute (i.e., USA or Europe).
		filterOp : str, optional
			Filter operation of interest.
			Possible values: '=', '<', '>', '<=', '>=', '!=', by default "="
		channel : str, optional
			Encoding channel where the specified attribute should be placed.
			Possible values: 'x','y','color', by default ""
		dataType : str, optional
			Data type for the specified attribute.
			Possible values: 'nominal', 'quantitative', 'ordinal','temporal', by default ""
		dataModel : str, optional
			Data model for the specified attribute
			Possible values: 'dimension', 'measure', by default ""
		aggregation : str, optional
			Aggregation function for specified attribute, by default ""
			Possible values: 'sum','mean', and others supported by Pandas.aggregate (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.aggregate.html), by default ""
		binSize : int, optional
			Number of bins for histograms, by default 0
		weight : float, optional
			A number between 0 and 1 indicating the importance of this Spec, by default 1
		sort : str, optional
			Specifying whether and how the bar chart should be sorted
			Possible values: 'ascending', 'descending', by default ""
		"""		
		# Descriptor
		self.description = description
		# Description gets compiled to attribute, value, filterOp
		self.attribute = attribute
		self.value = value
		self.filterOp = filterOp
		# self.parseDescription()
		# Properties
		self.channel = channel
		self.dataType = dataType
		self.dataModel = dataModel
		self.aggregation = aggregation
		self.binSize = binSize
		self.weight = weight
		self.sort = sort
			
	def __repr__(self):
		
		repr_string = f"Spec < \n"
		if self.description != "":
			repr_string += f"    description:{str(self.description)}\n"
		if self.channel != "":
			repr_string += f"    channel:{str(self.channel)}\n"
		if len(self.attribute) != 0:
			repr_string += f"    attribute:{str(self.attribute)}\n"
		if self.aggregation != "":
			repr_string += f"    aggregation:{str(self.aggregation)}\n"
		if len(self.value) != 0:
			repr_string += f"    value:{str(self.value)}\n"
		repr_string += f"   >\n"
		if self.dataModel != "":
			repr_string += f"   dataModel:{str(self.dataModel)}\n"
		if len(self.dataType) != 0:
			repr_string += f"   dataType:{str(self.dataType)}\n"
		if self.binSize != None:
			repr_string += f"   binSize:{str(self.binSize)}\n"
		return repr_string + "\n"

