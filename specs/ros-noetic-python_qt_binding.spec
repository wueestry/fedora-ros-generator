Name:           ros-noetic-python_qt_binding
Version:        noetic.0.4.4
Release:        1%{?dist}
Summary:        ROS package python_qt_binding

License:        BSD
URL:            http://www.ros.org/

Source0:        https://github.com/ros-gbp/python_qt_binding-release/archive/release/noetic/python_qt_binding/0.4.4-1.tar.gz#/ros-noetic-python_qt_binding-0.4.4-source0.tar.gz

Patch0: noetic/python_qt_binding.lflags-fix.patch

BuildArch: noarch

# common BRs
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gtest-devel
BuildRequires:  log4cxx-devel
BuildRequires:  python3-devel
BuildRequires:  python-unversioned-command

BuildRequires:  python3-pyside2
BuildRequires:  python3-qt5-devel sip
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ros-noetic-catkin-devel
BuildRequires:  ros-noetic-rosbuild-devel

Requires:       python3-pyside2

Provides:  ros-noetic-python_qt_binding = 0.4.4-1
Obsoletes: ros-noetic-python_qt_binding < 0.4.4-1
Obsoletes: ros-kinetic-python_qt_binding < 0.4.4-1



%description
This stack provides Python bindings for Qt. There are two providers:
pyside and pyqt. PySide is released under the LGPL. PyQt is released
under the GPL. Both the bindings and tools to build bindings are
included from each available provider. For PySide, it is called
"Shiboken". For PyQt, this is called "SIP". Also provided is adapter
code to make the user's Python code independent of which binding
provider was actually used which makes it very easy to switch between
these.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ros-noetic-catkin-devel
Requires:       python3-pyside2
Requires:       python3-qt5-devel sip
Requires:       qt5-qtbase-devel
Requires:       ros-noetic-rosbuild-devel

Provides: ros-noetic-python_qt_binding-devel = 0.4.4-1
Obsoletes: ros-noetic-python_qt_binding-devel < 0.4.4-1
Obsoletes: ros-kinetic-python_qt_binding-devel < 0.4.4-1


%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.



%prep

%setup -c -T
tar --strip-components=1 -xf %{SOURCE0}
%patch0 -p1

%build
# nothing to do here


%install

PYTHONUNBUFFERED=1 ; export PYTHONUNBUFFERED

CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ; \
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ; \
FFLAGS="${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FFLAGS ; \
FCFLAGS="${FCFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FCFLAGS ; \
%{?__global_ldflags:LDFLAGS="${LDFLAGS:-%__global_ldflags}" ; export LDFLAGS ;} \

source %{_libdir}/ros/setup.bash

# substitute shebang before install block because we run the local catkin script
%py3_shebang_fix .

DESTDIR=%{buildroot} ; export DESTDIR


catkin_make_isolated \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCATKIN_ENABLE_TESTING=OFF \
  -DPYTHON_VERSION=%{python3_version} \
  -DPYTHON_VERSION_NODOTS=%{python3_version_nodots} \
  --source . \
  --install \
  --install-space %{_libdir}/ros/ \
  --pkg python_qt_binding




rm -rf %{buildroot}/%{_libdir}/ros/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh}

touch files.list
find %{buildroot}/%{_libdir}/ros/{bin,etc,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros/{include,lib*/pkgconfig,share/python_qt_binding/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list

find . -maxdepth 1 -type f -iname "*readme*" | sed "s:^:%%doc :" >> files.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list



# replace cmake python macro in shebang
for file in $(grep -rIl '^#!.*@PYTHON_EXECUTABLE@.*$' %{buildroot}) ; do
  sed -i.orig 's:^#!\s*@PYTHON_EXECUTABLE@\s*:%{__python3}:' $file
  touch -r $file.orig $file
  rm $file.orig
done


echo "This is a package automatically generated with rosfed." >> README_FEDORA
echo "See https://pagure.io/ros for more information." >> README_FEDORA
install -m 0644 -p -D -t %{buildroot}/%{_docdir}/%{name} README_FEDORA
echo %{_docdir}/%{name} >> files.list
install -m 0644 -p -D -t %{buildroot}/%{_docdir}/%{name}-devel README_FEDORA
echo %{_docdir}/%{name}-devel >> files_devel.list

%py3_shebang_fix %{buildroot}

# Also fix .py.in files
for pyfile in $(grep -rIl '^#!.*python.*$' %{buildroot}) ; do
  %py3_shebang_fix $pyfile
done


%files -f files.list
%files devel -f files_devel.list


%changelog
* 2023-04-17 Ryan Wüest <ryan.wueest@protonmail.com> - noetic.0.4.4-1
- Initial desktop generation
