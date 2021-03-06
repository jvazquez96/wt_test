from flask_restplus import fields
from api.restplus import api
from api.submissions.serializers import last_submission

#submission
#create a problem
evaluator_submission = api.model('SubmissionCreation', {
    'request_type': fields.String(required=True,description='Evaluation type, must be \'submission\' in this case'),
    'problem_id': fields.Integer(required=True, description='The unique identifier of the Problem'),
    'code': fields.String(required=True, description='Student\'s code to be executed'),
    'language': fields.String(required=True, description='Language of the code to be executed'),
    'user_id': fields.Integer(required=True, description='Id of the submitting user')
})

problem_evaluation = api.model('ProblemEvalution', {
    'name': fields.String(required=True, description='Problem name, required to verify uniqueness'),
    'request_type': fields.String(required=True, description='Evaluation type, must be \'upload\' in this case'),
    'code': fields.String(required=True, description='Student\'s code to be executed'),
    'language': fields.String(required=True, description='Language of the code to be executed'),
    'time_limit': fields.Integer(required=True, description='Number of seconds before TLE'),
    'memory_limit': fields.Integer(required=True, description='Number of KBs before MLE'),
    'is_update': fields.Boolean(required=False, description='Flag that indicates if problem is being updated'),
    'test_cases': fields.List(cls_or_instance=fields.String, required=True, description='Array of strings containing the test cases\' input')
})

case_creation = api.model('CaseCreation', {
    'input': fields.String(required=True, description='Test case input'),
    'feedback': fields.String(required=True, description='Test case feedback'),
    'output': fields.String(required=True, description='Test case expected output'),
    'is_sample': fields.Boolean(required=True, description='Flag that tells if test case will appear as sample')
  })

problem_creation = api.model('ProblemCreation', {
    'author_id': fields.Integer(required=True, description='Id of the submitting user'),
    'name': fields.String(required=True, description='Problem name'),
    'description_english': fields.String(required=True, description='Problem description in English'),
    'description_spanish': fields.String(required=True, description='Problem description in Spanish'),
    'code': fields.String(required=True, description='Student\'s code to be executed'),
    'language': fields.String(required=True, description='Language of the code to be executed'),
    'difficulty': fields.Integer(required=True, description='Problem difficulty'),
    'time_limit': fields.Integer(required=True, description='Number of seconds before TLE'),
    'memory_limit': fields.Integer(required=True, description='Number of KBs before MLE'),
    'topic_id': fields.Integer(required=True, description='Problem\'s topic'),
    'type': fields.String(required=True, description='Problem type'),
    'test_cases': fields.List(fields.Nested(case_creation), required=True, description='Array of strings containing the test cases\' input'),
    'belongs_to': fields.Integer(required=True, description='Parent problem'),
    'is_subproblem': fields.Boolean(required=True, description='Is the problem a function or subproblem?')
})

evaluator_result = api.model('Result', {
    'status': fields.String(required=True, description='Compilation status'),
    'test_cases': fields.List(cls_or_instance=fields.String, required=True, description='Array of strings containing the test cases\' results')
})

problem_submission = api.model('ProblemSubmission', {
    'status': fields.String(required=True, description='Submission status'),
    'attempts': fields.List(fields.Nested(last_submission), required=False, description='Array of objects containing the last 3 attempts')
})
