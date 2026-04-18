from setuptools import setup
import setup_translate

pkg = 'Extensions.GBIpboxClient'
setup(name='enigma2-plugin-extensions-gbipboxclient',
       version='1.0',
       description='GBIpboxClient',
       package_dir={pkg: 'GBIpboxClient'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
