tokens = {
    "access_token": {
        "access_token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..IIqIjcZLRq-IJ-GomGsjqg.XPJ-zEzfrQQ3RXU6apQsTOubNHgi1oTcnCHUzE8xrPrzahZg7ciMkmpoTBtlJA7OSiiJXlsc5dtpx-MTqCrxdoETzPodtvkm06xDLOaIxAROj4MS.QmQBEq8rIMWh7E2d8oj2rw",
        "token_type": "bearer"
    },
    "refresh_token": {
        "access_token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..FQxCZvNC2Ql8ubhw7Sl01g.IK9qdTXzqztZinexeIymRE0Jka9wgU2gG5nRh2sJ24qjVQdUaClILeuNmuNdJ_Di1OH8preUcsXn7Em-LWiBHhMssIHoTG2-3iq9kY5OuEBNDKvxuA.njDxRu79rCBum_H7UPzZgw",
        "token_type": "refresh"
    }
}

aTok  = tokens["access_token"]["access_token"]
rTok  = tokens["refresh_token"]["access_token"]

from jose import jwe, jws, jwt

def decode_access_token(authorisation_token):
    TEST = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..jwv1zIaiPCcji0-lT4MF9A.PEM0NQ5LuicwWqDvzvAoIlpHq3d6R5dt_rOJbrLvXV12pI4cMy3ooCGiiROOTFRkdnj_cge9a29Wm5QatccgJ7U9ao_YBW6Az33Vn4o2RjiRPiAFJA.OzmRfSDdsmZXM0UkhafsfA"
    TEST2= "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..yta4b2GIgWE62x-bEjkVBg.ymXYrMxrC4PxYUnZl5la5MfoseWcxQgID-vaD2OgbdeC7xRpxgOykirjbqfnlbCL30gsRNTudRjqcc7s3IPSc7XBRU9gNyxUTGqrKW82v5SjCjnU.g1CzngLUoI8aG32Fd3dfqQe"
    TEST2= "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..RQEWaFb_T06bCV7TPf874g.0YGh9jtMDGSMVo8obR8mfldoSboRhFQNLP3FqNlGZyn3_yW-8CdyqQbvsLp3xkjNH30ulOaDXVZCeZkULmKUJ9ojnGt4.kkTwu7Q7wWJ9Vb9y-mOd3A"
    #print(authorisation_token)
    #print(TEST)
    print(TEST2)
    # get public key from jwks uri

    # gives the set of jwks keys.the keys has to be passed as it is to jwt.decode() for signature verification.
    key = b'y\xf8l\xf3\xf7n\xd5y\xcf]N\xd4P;\nuy\xa2\x96\xc6\xc6~@\x00\x96\rn\x1dq]\x12\xd6'

    # get the algorithm type from the request header
    #algorithm = jwt.get_unverified_header(authorisation_token).get('alg')
    #print(jwt.get_unverified_header(TEST))
    print(jwt.get_unverified_header(TEST2))

    user_info = jwe.decrypt(TEST2,
                           key=key)

    return user_info


print(decode_access_token(rTok))

#print(decode_access_token(rTok))