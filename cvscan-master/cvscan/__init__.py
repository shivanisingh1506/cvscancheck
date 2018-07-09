#!/usr/bin/env python
"""

Main program

"""

import converter
import annotations_parser
import details_parser as dp
import language_parser as lp
import json
import dirpath
import configurations

import pydocumentdb.documents as documents
import pydocumentdb.document_client as document_client
import pydocumentdb.errors as errors
import datetime
import config as cfg


#This here is defined the CosmosDB parameters

HOST = cfg.settings['host']

MASTER_KEY = cfg.settings['master_key']

DATABASE_ID = cfg.settings['database_id']

COLLECTION_ID = cfg.settings['collection_id']


database_link = 'dbs/' + DATABASE_ID

collection_link = database_link + '/colls/' + COLLECTION_ID


class IDisposable:

    """ A context manager to automatically close an object with a close method

    in a with statement. """



    def __init__(self, obj):

        self.obj = obj



    def __enter__(self):

        return self.obj # bound to target



    def __exit__(self, exception_type, exception_val, trace):

        # extra cleanup in here

        self = None


class Cvscan():


    def __init__(self, name, path = dirpath.RESUMEPATH):
        self.path = path + '/' + name + '.pdf'
        self.path = name + '.pdf'

        if self.exists():
            self.extract()
        else:
            raise OSError("There is no file found at " + self.path)

    def exists(self):
        return configurations.isfile(self.path)

    # Extracts raw text from resume
    # Currently only supports PDF
    def extract(self):
        # add functions to convert other formats to text
        if self.path.find(".pdf") != -1:
            self.raw_text = converter.pdf_to_txt(self.path)

        if self.raw_text is not '':
            self.parse()
        else:
            raise ValueError("Error extracting resume text.")

    def parse(self):
        self.URLs = annotations_parser.fetch_pdf_urls(self.path)
        self.name = lp.fetch_name(self.raw_text)
        self.emails = dp.fetch_email(self.raw_text)
        self.phone_numbers = dp.fetch_phone(self.raw_text)
        self.address = dp.fetch_address(self.raw_text)
        self.experience = dp.calculate_experience(self.raw_text)
        self.cleaned_resume = lp.clean_resume(self.raw_text)
        self.skills = dp.fetch_skills(self.cleaned_resume)
        (self.qualifications,self.degree_info) = dp.fetch_qualifications(
            self.raw_text)
        self.job_positions, self.category = dp.fetch_jobs(self.cleaned_resume)
        self.current_employers,self.employers = lp.fetch_employers(
            self.raw_text,self.job_positions)
        self.extra_info = dp.fetch_extra(self.raw_text)

    # TODO: Add more fetch here
    def show(self):
        return json.dumps({
            "name" : self.name,
            "experience" : self.experience,
            "address" : self.address,
            "phone_numbers" : self.phone_numbers,
            "emails" : self.emails,
            "urls" : self.URLs,
            "skills" : self.skills,
            "jobs" : self.job_positions,
            "job category" : self.category,
            "employers" : self.employers,
            "current_employers" : self.current_employers,
            "qualifications" : self.qualifications,
            "qualifications_info" : self.degree_info,
            "extra_info" : self.extra_info
        })
		
		
    @staticmethod

    def CreateDocuments(self):

        print('Creating Documents')


        # Create a SalesOrder object. This object has nested properties and various types including numbers, DateTimes and strings.

        # This can be saved as JSON as is without converting into rows/columns.
        
        resume1 = Cvscan.show(self)
       
        self.CreateDocument(collection_link,resume1)
		
		
		
		  @staticmethod

    def ReadDocuments(self):

        print('\n1.3 - Reading all documents in a collection\n')



        # NOTE: Use MaxItemCount on Options to control how many documents come back per trip to the server

        #       Important to handle throttles whenever you are doing operations such as this that might

        #       result in a 429 (throttled request)

        documentlist = list(self.ReadDocuments(collection_link, {'maxItemCount':10}))

        

        print('Found {0} documents'.format(documentlist.__len__()))

        

        for doc in documentlist:

            print('Document Id: {0}'.format(doc.get('name')))
			
			
			
		def run_sample():

             with IDisposable(document_client.DocumentClient(HOST, {'masterKey': MASTER_KEY} )) as self :

				try:

					# setup database for this sample

					try:

						self.CreateDatabase({"id": DATABASE_ID})



					except errors.DocumentDBError as e:

						if e.status_code == 409:

							pass

						else:

							raise errors.HTTPFailure(e.status_code)



            # setup collection for this sample

				try:

					self.CreateCollection(database_link, {"id": COLLECTION_ID})

					print('Collection with id \'{0}\' created'.format(COLLECTION_ID))



				except errors.DocumentDBError as e:

					if e.status_code == 409:

						print('Collection with id \'{0}\' was found'.format(COLLECTION_ID))

					else:

						raise errors.HTTPFailure(e.status_code)



				Cvscan.CreateDocuments(self)

				Cvscan.ReadDocuments(self)



			except errors.HTTPFailure as e:
	
				print('\nrun_sample has caught an error. {0}'.format(e.message))

        

			finally:

				print("\nrun_sample done")



if __name__ == '__main__':

    try:

        run_sample()



    except Exception as e:

        print("Top level Error: args:{0}, message:N/A".format(e.args))
