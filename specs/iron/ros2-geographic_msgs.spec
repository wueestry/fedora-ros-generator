Name:           ros2-iron-geographic_msgs
Version:        1.0.6
Release:        1%{?dist}
Summary:        ROS package geographic_msgs

License:        BSD
URL:            http://www.ros.org/

Source0:        https://github.com/ros2-gbp/geographic_info-release/archive/release/iron/geographic_msgs/1.0.6-1.tar.gz#/ros2-iron-geographic_msgs-1.0.6-source0.tar.gz



# common BRs
BuildRequires: patchelf
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: make
BuildRequires: patch
BuildRequires: python3-devel
BuildRequires: python-unversioned-command
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

BuildRequires:  ros2-iron-ament_cmake-devel
BuildRequires:  ros2-iron-ament_cmake_cppcheck-devel
BuildRequires:  ros2-iron-ament_cmake_cpplint-devel
BuildRequires:  ros2-iron-ament_cmake_gtest-devel
BuildRequires:  ros2-iron-ament_cmake_lint_cmake-devel
BuildRequires:  ros2-iron-ament_cmake_uncrustify-devel
BuildRequires:  ros2-iron-ament_cmake_xmllint-devel
BuildRequires:  ros2-iron-ament_lint_auto-devel
BuildRequires:  ros2-iron-ament_package-devel
BuildRequires:  ros2-iron-geometry_msgs-devel
BuildRequires:  ros2-iron-rosidl_default_generators-devel
BuildRequires:  ros2-iron-std_msgs-devel
BuildRequires:  ros2-iron-unique_identifier_msgs-devel

Requires:       ros2-iron-geometry_msgs
Requires:       ros2-iron-rosidl_default_runtime
Requires:       ros2-iron-std_msgs
Requires:       ros2-iron-unique_identifier_msgs

Provides:  ros2-iron-geographic_msgs = 1.0.6-1
Obsoletes: ros2-iron-geographic_msgs < 1.0.6-1



%description
ROS messages for Geographic Information Systems.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ros2-iron-ament_cmake-devel
Requires:       ros2-iron-ament_cmake_cppcheck-devel
Requires:       ros2-iron-ament_cmake_cpplint-devel
Requires:       ros2-iron-ament_cmake_gtest-devel
Requires:       ros2-iron-ament_cmake_lint_cmake-devel
Requires:       ros2-iron-ament_cmake_uncrustify-devel
Requires:       ros2-iron-ament_cmake_xmllint-devel
Requires:       ros2-iron-ament_lint_auto-devel
Requires:       ros2-iron-ament_package-devel
Requires:       ros2-iron-geometry_msgs-devel
Requires:       ros2-iron-rosidl_default_generators-devel
Requires:       ros2-iron-std_msgs-devel
Requires:       ros2-iron-unique_identifier_msgs-devel
Requires:       ros2-iron-rosidl_default_runtime-devel

Provides: ros2-iron-geographic_msgs-devel = 1.0.6-1
Obsoletes: ros2-iron-geographic_msgs-devel < 1.0.6-1


%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.



%prep

%setup -c -T
tar --strip-components=1 -xf %{SOURCE0}

%build
# nothing to do here


%install

PYTHONUNBUFFERED=1 ; export PYTHONUNBUFFERED
GZ_BUILD_FROM_SURCE=1; export GZ_BUILD_FROM_SOURCE

CFLAGS=" -Wno-error ${CFLAGS:-%optflags} -Wno-error -w -Wno-error=int-conversion" ; export CFLAGS ; \
CXXFLAGS=" -Wno-error ${CXXFLAGS:-%optflags} -Wno-error -w -Wno-error=int-conversion" ; export CXXFLAGS ; \
FFLAGS=" -Wno-error ${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}} -w -Wno-error=int-conversion" ; export FFLAGS ; \
FCFLAGS="${FCFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}} -w -Wno-error=int-conversion" ; export FCFLAGS ; \
%{?__global_ldflags:LDFLAGS="${LDFLAGS:-%__global_ldflags}" ; export LDFLAGS ;} \

source %{_libdir}/ros2-iron/setup.bash

# substitute shebang before install block because we run the local catkin script
%py3_shebang_fix .

# DESTDIR=%{buildroot} ; export DESTDIR


colcon \
  build \
  --merge-install \
  --cmake-args -DPYTHON_EXECUTABLE="/usr/bin/python" \
  -DTHIRDPARTY_Asio=ON \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_CXX_FLAGS="$CXXFLAGS" \
  -DCMAKE_C_FLAGS="$CFLAGS" \
  -DCMAKE_LD_FLAGS="$LDFLAGS" \
  -DBUILD_TESTING=OFF \
  --base-paths . \
  --install-base %{buildroot}/%{_libdir}/ros2-iron/ \
  --packages-select geographic_msgs



# remove wrong buildroot prefixes
find %{buildroot}/%{_libdir}/ros2-iron/ -type f -exec sed -i "s:%{buildroot}::g" {} \;

# # Move include directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-iron/opt/geographic_msgs/include ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-iron/include/geographic_msgs ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-iron/include/geographic_msgs
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-iron/opt/geographic_msgs/include/* %{buildroot}/%{_libdir}/ros2-iron/include/geographic_msgs
# fi
# 
# # Move share directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-iron/opt/geographic_msgs/share ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-iron/share ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-iron/share
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-iron/opt/geographic_msgs/share %{buildroot}/%{_libdir}/ros2-iron/
#     find %{buildroot}/%{_libdir}/ros2-iron/share -type f -exec sed -i "s:opt/geographic_msgs/::g" {} \;
# fi
# 
# # Move bin directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-iron/opt/geographic_msgs/bin ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-iron/bin ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-iron/bin
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-iron/opt/geographic_msgs/bin %{buildroot}/%{_libdir}/ros2-iron/
# fi
# 
# # Move extra_cmake directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-iron/opt/geographic_msgs/extra_cmake ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-iron/extra_cmake ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-iron/extra_cmake
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-iron/opt/geographic_msgs/extra_cmake %{buildroot}/%{_libdir}/ros2-iron/
#     find %{buildroot}/%{_libdir}/ros2-iron/extra_cmake -type f -exec sed -i "s:opt/geographic_msgs/::g" {} \;
# fi
# 
# # Move lib directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-iron/opt/geographic_msgs/lib ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-iron/lib ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-iron/lib
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-iron/opt/geographic_msgs/lib %{buildroot}/%{_libdir}/ros2-iron/lib
# fi
# 
# # Move lib64 directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-iron/opt/geographic_msgs/lib64 ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-iron/lib64 ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-iron/lib64
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-iron/opt/geographic_msgs/lib64 %{buildroot}/%{_libdir}/ros2-iron/lib64
# fi

rm -rf %{buildroot}/%{_libdir}/ros2-iron/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

# remove __pycache__
find %{buildroot} -type d -name '__pycache__' -exec rm -rf {} +
find . -name '*.pyc' -delete

touch files.list
find %{buildroot}/%{_libdir}/ros2-iron/{opt,bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros2-iron/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros2-iron/{lib*/pkgconfig,include/,cmake/,geographic_msgs/include/,share/geographic_msgs/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list

find . -maxdepth 1 -type f -iname "*readme*" | sed "s:^:%%doc :" >> files.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list



find %{buildroot}/%{_libdir}/ros2-iron/ -name *__rosidl_generator_py.so -type f -exec patchelf --remove-rpath  {} \;
# find %{buildroot}/%{_libdir}/ros2-iron/ -name *__rosidl_generator_py.so -type f -exec patchelf --force-rpath --add-rpath "%{_libdir}/ros2/lib" {} \;

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
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.0.6-1
- Update to latest release
