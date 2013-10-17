####Queries

#get unique sequences among donors, group by length of sequence too
query_1 = [{"$match" : {"cdr3_seq_aa_len" : {"$gt":0}}},
{"$group": 
         {
              "_id": {"donor": "$donor", "cdr3_seq_aa": "$cdr3_seq_aa"},
              "donor_cdr3_seq_aa_count": {"$sum": 1},
              "cdr3_seq_aa_len": {"$first": "$cdr3_seq_aa_len"}
         }},
{"$group":
  			 {
           "_id": {"len": "$cdr3_seq_aa_len"},
						"unique_cdr3_group_donor_first": {"$sum": 1},
						"total_read_of_this_length": {"$sum": "$donor_cdr3_seq_aa_count"}
						}
   }]


#get unique sequences when we pool all of the CDR3s, then group by length
query_2 = [{"$match" : {"cdr3_seq_aa_len" : {"$gt":0}}},
{"$group": 
         {
              "_id": {"cdr3_seq_aa": "$cdr3_seq_aa"},
              "donor_cdr3_seq_aa_count": {"$sum": 1},
              "cdr3_seq_aa_len": {"$first": "$cdr3_seq_aa_len"}
         }},
{"$group":
  			 {
           "_id": {"len": "$cdr3_seq_aa_len"},
						"unique_cdr3_pool_cdr3": {"$sum": 1},
						"total_read_of_this_length": {"$sum": "$donor_cdr3_seq_aa_count"}
						}
   }]


#get unique sequences, then count up how many unique sequences in every donor
query_3 = [{"$match" : {"cdr3_seq_aa_len" : {"$gt":3}}},
{"$group": 
         {
              "_id": {"donor": "$donor", "cdr3_seq_aa": "$cdr3_seq_aa"}
         }},
{"$group":
             {
           "_id": {"donor": "$_id.donor"},
                        "how_many_unique_for_this_donor": {"$sum": 1}
                        }
   }]

#get_distrobution
query_4 = {"$group":{"_id":"$cdr3_aa_length", "sum":{"$sum":1}}}
