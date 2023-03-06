Name:           ros2-catkin
Version:        noetic.0.8.10
Release:        1%{?dist}
Summary:        ROS package catkin

License:        BSD
URL:            http://wiki.ros.org/catkin

Source0:        https://github.com/ros-gbp/catkin-release/archive/release/noetic/catkin/0.8.10-1.tar.gz#/ros2-noetic-catkin-0.8.10-source0.tar.gz

Patch0: ros-kinetic-catkin.python-path-in-templates.patch
Patch1: ros-catkin.python3.patch

BuildArch: noarch

# common BRs
BuildRequires: patchelf
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: make
BuildRequires: patch
BuildRequires: python3-devel
BuildRequires: python-unversioned-command
BuildRequires: ros2-ament_package
BuildRequires: python3-colcon-common-extensions
BuildRequires: python3-pip
BuildRequires: python3-pydocstyle
BuildRequires: python3-pytest
BuildRequires: python3-pytest-repeat
BuildRequires: python3-pytest-rerunfailures
BuildRequires: python3-rosdep
BuildRequires: python3-setuptools
BuildRequires: python3-vcstool

# BuildRequires:  boost-devel
# BuildRequires:  console-bridge-devel
# BuildRequires:  gtest-devel
# BuildRequires:  log4cxx-devel
# BuildRequires:  python3-devel
# BuildRequires:  python3-colcon-common-extensions
# BuildRequires:  python-unversioned-command

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  python3
BuildRequires:  python3-catkin_pkg
BuildRequires:  python3-empy
BuildRequires:  python3-mock
BuildRequires:  python3-nose
BuildRequires:  python3-pyparsing
BuildRequires:  python3-setuptools
BuildRequires:  ros2-noetic-ament_package-devel

Requires:       python3
Requires:       python3-catkin_pkg
Requires:       python3-empy
Requires:       python3-pyparsing

Provides:  ros2-noetic-catkin = 0.8.10-1
Obsoletes: ros2-noetic-catkin < 0.8.10-1


Obsoletes: ros-kdl_parser_py < melodic.1.13.1-4
Obsoletes: ros-orocos_kdl < melodic.1.4.0-4
Obsoletes: ros-python_orocos_kdl < melodic.1.4.0-6

%description
Low-level build system macros and infrastructure for ROS.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       cmake
Requires:       gmock-devel
Requires:       gtest-devel
Requires:       python3-nose
Requires:       python3-setuptools
Requires:       gcc-c++
Requires:       python3
Requires:       python3-catkin_pkg
Requires:       python3-empy
Requires:       python3-mock
Requires:       python3-pyparsing
Requires:       ros2-noetic-ament_package-devel

Provides: ros2-noetic-catkin-devel = 0.8.10-1
Obsoletes: ros2-noetic-catkin-devel < 0.8.10-1

Obsoletes: ros-kdl_parser_py-devel < melodic.1.13.1-4
Obsoletes: ros-orocos_kdl-devel < melodic.1.4.0-4
Obsoletes: ros-python_orocos_kdl-devel < melodic.1.4.0-6

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.



%prep

%setup -c -T
tar --strip-components=1 -xf %{SOURCE0}
%patch0 -p1
%patch1 -p1

%build
# nothing to do here


%install

PYTHONUNBUFFERED=1 ; export PYTHONUNBUFFERED

CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ; \
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ; \
FFLAGS="${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FFLAGS ; \
FCFLAGS="${FCFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FCFLAGS ; \
%{?__global_ldflags:LDFLAGS="${LDFLAGS:-%__global_ldflags}" ; export LDFLAGS ;} \


# substitute shebang before install block because we run the local catkin script
%py3_shebang_fix .

# DESTDIR=%{buildroot} ; export DESTDIR

./bin/catkin_make_isolated \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCATKIN_ENABLE_TESTING=OFF \
  --source . \
  --install \
  --install-space %{_libdir}/ros/ \
  --pkg catkin


touch files.list
find %{buildroot}/%{_libdir}/ros/{bin,etc,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros/{include,lib*/pkgconfig} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list

find %{buildroot}/%{_libdir}/ros -maxdepth 1 \
  -name .catkin -o -name .rosinstall \
  -o -name "_setup*" -o -name "setup.*" -o -name "local_setup.*" -o -name env.sh \
  | sed -e "s:%{buildroot}/::" -e "s:.py$:.py{,o,c}:" >> files.list

find . -maxdepth 1 -type f -iname "*readme*" | sed "s:^:%%doc :" >> files.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list



find %{buildroot}/%{_libdir}/ros2/ -name *__rosidl_generator_py.so -type f -exec patchelf --remove-rpath  {} \;
find %{buildroot}/%{_libdir}/ros2/ -name *__rosidl_generator_py.so -type f -exec patchelf --add-rpath "%{_libdir}/ros2/lib" {} \;

# replace cmake python macro in shebang
for file in $(grep -rIl '^#!.*@PYTHON_EXECUTABLE@.*$' %{buildroot}) ; do
  sed -i.orig 's:^#!\s*@PYTHON_EXECUTABLE@\s*:%{__python3}:' $file
  touch -r $file.orig $file
  rm $file.orig
done


echo "This is a package automatically generated with rosfed." >> README_FEDORA
echo "See  https://github.com/morxa/rosfed for more information." >> README_FEDORA
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
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.8.10-1
- update to latest release
