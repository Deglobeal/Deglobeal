# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Add this line to specify the directory where static files will be collected
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
