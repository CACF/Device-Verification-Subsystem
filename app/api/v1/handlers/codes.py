"""
 Copyright (c) 2018 Qualcomm Technologies, Inc.                                                                      #
                                                                                                                     #
 All rights reserved.                                                                                                #
                                                                                                                     #
 Redistribution and use in source and binary forms, with or without modification, are permitted (subject to the      #
 limitations in the disclaimer below) provided that the following conditions are met:                                #
 * Redistributions of source code must retain the above copyright notice, this list of conditions and the following  #
   disclaimer.                                                                                                       #
 * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the         #
   following disclaimer in the documentation and/or other materials provided with the distribution.                  #
 * Neither the name of Qualcomm Technologies, Inc. nor the names of its contributors may be used to endorse or       #
   promote products derived from this software without specific prior written permission.                            #
                                                                                                                     #
 NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY THIS LICENSE. THIS SOFTWARE IS PROVIDED  #
 BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED #
 TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT      #
 SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR   #
 CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES LOSS OF USE,      #
 DATA, OR PROFITS OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,      #
 STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,   #
 EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                                                                  #
"""

RESPONSES = {
    'NOT_FOUND': 404,
    'BAD_REQUEST': 400,
    'OK': 200,
    'NO_CONTENT': 204,
    'INTERNAL_SERVER_ERROR': 500,
    'SERVICE_UNAVAILABLE': 503,
    'TIMEOUT': 504,
    'METHOD_NOT_ALLOWED': 405
}

MESSAGES = {
    'NOT_FOUND': 'Resource not found.',
    'BAD_REQUEST': 'Bad Format',
    'OK': 'Executed successfully',
    'INTERNAL_SERVER_ERROR': 'There is some internal error',
    'METHOD_NOT_ALLOWED': 'Method not allowed.'
}

MIME_TYPES = {
    'JSON': 'application/json',
    'TEXT': 'text/plain',
    'ALL': 'application/*'
}
