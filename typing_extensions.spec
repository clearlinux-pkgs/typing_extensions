#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : typing_extensions
Version  : 3.7.4.3
Release  : 23
URL      : https://files.pythonhosted.org/packages/16/06/0f7367eafb692f73158e5c5cbca1aec798cdf78be5167f6415dd4205fa32/typing_extensions-3.7.4.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/16/06/0f7367eafb692f73158e5c5cbca1aec798cdf78be5167f6415dd4205fa32/typing_extensions-3.7.4.3.tar.gz
Summary  : Backported and Experimental Type Hints for Python 3.5+
Group    : Development/Tools
License  : Python-2.0
Requires: typing_extensions-license = %{version}-%{release}
Requires: typing_extensions-python = %{version}-%{release}
Requires: typing_extensions-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
The ``typing`` module was added to the standard library in Python 3.5 on
        a provisional basis and will no longer be provisional in Python 3.7. However,
        this means users of Python 3.5 - 3.6 who are unable to upgrade will not be
        able to take advantage of new types added to the ``typing`` module, such as
        ``typing.Text`` or ``typing.Coroutine``.
        
        The ``typing_extensions`` module contains both backports of these changes
        as well as experimental types that will eventually be added to the ``typing``
        module, such as ``Protocol`` or ``TypedDict``.
        
        Users of other Python versions should continue to install and use
        the ``typing`` module from PyPi instead of using this one unless specifically
        writing code that must be compatible with multiple Python versions or requires
        experimental types.

%package license
Summary: license components for the typing_extensions package.
Group: Default

%description license
license components for the typing_extensions package.


%package python
Summary: python components for the typing_extensions package.
Group: Default
Requires: typing_extensions-python3 = %{version}-%{release}

%description python
python components for the typing_extensions package.


%package python3
Summary: python3 components for the typing_extensions package.
Group: Default
Requires: python3-core
Provides: pypi(typing_extensions)

%description python3
python3 components for the typing_extensions package.


%prep
%setup -q -n typing_extensions-3.7.4.3
cd %{_builddir}/typing_extensions-3.7.4.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598286252
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/typing_extensions
cp %{_builddir}/typing_extensions-3.7.4.3/LICENSE %{buildroot}/usr/share/package-licenses/typing_extensions/7ad627868f90ad068bd06801aab97ec1ca34b890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/typing_extensions/7ad627868f90ad068bd06801aab97ec1ca34b890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
