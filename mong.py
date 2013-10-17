import pymongo as pm

def get_current_op(print_verbose=True):
	conn = pm.Connection()
	to_pretty = conn.admin["$cmd.sys.inprog"].find_one()
	for i in sorted(to_pretty['inprog']):
		for j in i:
			if print_verbose:
				print j, i[j]
	return to_pretty['inprog']

def kill_all_processes():
	conn = pm.Connection()
	process = get_current_op(print_verbose=False)
	for i in process:
		print i['opid']



def init(database="64_donors_with_junctions",collect="unique",type="collect",max_pool_size=16):
	"""initialize_your_database, return a collect
	,return the handler\
	mong.init(database,collect=uniq,type=collect)
	where database is the name of your database
	collection is the collection
	type will return a collection or database"""
	if type == "database":
		return pm.MongoClient(max_pool_size=max_pool_size)[database]
	elif type == "collect":
		return pm.MongoClient(max_pool_size=max_pool_size)[database][collect]
	else:
		print "Type must be a collect or a database"

def print_aggregate(cursor_object):
	"""prints out nice pretty sorted aggregate result"""
	for object in sorted(cursor_object['result']):
		keys = object.iterkeys()
		print object['_id'],"\t",
		for key in keys:
			if key != "_id":
				print object[key],
		print
		
def save_aggregate(cursor_object,output="aggregate_out.txt"):
	"""saves the aggregate output to a nice text file"""
	with open(output,'w') as f:
		for objects in sorted(cursor_object['result']):
			ids = objects.keys()
			for i in ids:
				f.write(str(objects[i])+"\t\t")
			f.write("\n")

def print_cursor(cursor_object, headers = True,use_generator=False,id="_id"):
	"""prints out nice pretty sorted find result"""
	if use_generator == False:
		#it is probably ok to store the cursor object in list memory since its a find result
		cursor_object = [x for x in cursor_object]
		if headers:
			print "  ".join([id]+sorted(cursor_object[0]['value'].iterkeys()))
        	for object in sorted(cursor_object):
			print object['_id'],
			for i in sorted(object['value']):
				print object['value'][i],
			#print object['_id'], 
			#print "\t".join(object['value'].itervalues())
                	print 
	else: #wants generator
		for object in cursor_object:
			for value in object.itervalues():
				print "hello"
				print str(value)+"\t",
			print
			
def get_fasta_file(aggregate_object,outfile="out.fasta"):
	"""outputs a fasta file from an aggregate object"""
	with open(outfile,'w') as f:
		for i,j in enumerate(aggregate_object['result'],start=1):
			current = ">{0}\n{1}\n".format(i,j['_id'])
			f.write(current)
def update_with_postion_id(cursor,collect):
	new_dictionary = {}
	for i in cursor:
		current_positions = {}
		for position,letter in enumerate(i["cdr3_seq_aa"],start=96):
			position = str(position)
			current_positions[position]=letter
		new_dictionary[i["_id"]]=current_positions
		
	for id in new_dictionary:
		#for seq in new_dictionary[id]:
		collect.update({"_id":id},{"$set":{"positions":new_dictionary[id]}})

def rev_comp(string):
	lookup = {'A':'T','C':'G','G':'C','T':'A','N':'N'}
 	return_string = [] 
	for i in string[::-1]:
		return_string.append(lookup[i])
	return "".join(return_string)

def get_cluster_info_grouped_by_cdr3_seq(collection_handle,cluster):
	cluster = collection_handle.aggregate([
		{"$match":
			{"design_cluster":cluster}
		},
		{"$group":
			{"_id":"$cdr3_seq",
			 "raw_seqs":{
					"$addToSet":"$raw_seq"
				    },
			 "cdr3_name":{
					"$addToSet":"$cdr3_name"
				     },
			 "donor" : {
					"$push":"$donor"
				   },
			"j-gene" : {
					"$addToSet":"$jg"
				   },
			"d-gene" : {
					"$addToSet":"$dg"
				   }
			}
		}])
	return cluster['result']
def print_out_fasta_of_cluster(cluster_handle,rc=True,cdr3=True):
	if rc and cdr3:
		for entry in cluster_handle:
			print ">{0}_{1}\n{2}".format(entry['cdr3_name'][0],entry['donor'][0],rev_comp(entry['_id']))
	elif rc and cdr3 is False:	
		for entry in cluster_handle:
			print ">{0}_{1}\n{2}".format(entry['cdr3_name'][0],entry['donor'][0],rev_comp(entry['raw_seqs'][0]))
	elif rc is False and cdr3:		
		for entry in cluster_handle:
			print ">{0}_{1}\n{2}".format(entry['cdr3_name'][0],entry['donor'][0],entry['_id'])
	else:
		for entry in cluster_handle:
			print ">{0}_{1}\n{2}".format(entry['cdr3_name'][0],entry['donor'][0],entry['raw_seqs'][0])
def print_out_gene_sets(cluster_handle):
	j_set = set()
	d_set = set()
	for entry in cluster_handle:
		j_set.add(entry['j-gene'][0])
		d_set.add(entry['d-gene'][0])

	print "J_genes ---> {0}\nD_Genes ---> {1}".format(j_set,d_set)
		
