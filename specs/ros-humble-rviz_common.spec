Name:           ros-humble-rviz_common
Version:        humble.11.2.5
Release:        1%{?dist}
Summary:        ROS package rviz_common

License:        BSD
URL:            https://github.com/ros2/rviz/blob/ros2/README.md

Source0:        https://github.com/ros2-gbp/rviz-release/archive/release/humble/rviz_common/11.2.5-1.tar.gz#/ros2-humble-rviz_common-11.2.5-source0.tar.gz

Patch0: ros-rviz_common.system-yaml-cpp.patch


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

BuildRequires:  qt5-qtbase-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  ros2-humble-ament_cmake-devel
BuildRequires:  ros2-humble-ament_cmake_cppcheck-devel
BuildRequires:  ros2-humble-ament_cmake_cpplint-devel
BuildRequires:  ros2-humble-ament_cmake_gmock-devel
BuildRequires:  ros2-humble-ament_cmake_gtest-devel
BuildRequires:  ros2-humble-ament_cmake_lint_cmake-devel
BuildRequires:  ros2-humble-ament_cmake_uncrustify-devel
BuildRequires:  ros2-humble-ament_cmake_xmllint-devel
BuildRequires:  ros2-humble-ament_lint_auto-devel
BuildRequires:  ros2-humble-ament_package-devel
BuildRequires:  ros2-humble-geometry_msgs-devel
BuildRequires:  ros2-humble-message_filters-devel
BuildRequires:  ros2-humble-pluginlib-devel
BuildRequires:  ros2-humble-rclcpp-devel
BuildRequires:  ros2-humble-resource_retriever-devel
BuildRequires:  ros2-humble-rviz_ogre_vendor-devel
BuildRequires:  ros2-humble-rviz_rendering-devel
BuildRequires:  ros2-humble-sensor_msgs-devel
BuildRequires:  ros2-humble-std_msgs-devel
BuildRequires:  ros2-humble-tf2-devel
BuildRequires:  ros2-humble-tf2_geometry_msgs-devel
BuildRequires:  ros2-humble-tf2_ros-devel
BuildRequires:  ros2-humble-tinyxml2_vendor-devel
BuildRequires:  ros2-humble-urdf-devel

Requires:       qt5-qtbase
Requires:       qt5-qtbase-gui
Requires:       yaml-cpp-devel
Requires:       ros2-humble-geometry_msgs
Requires:       ros2-humble-message_filters
Requires:       ros2-humble-pluginlib
Requires:       ros2-humble-rclcpp
Requires:       ros2-humble-resource_retriever
Requires:       ros2-humble-rviz_ogre_vendor
Requires:       ros2-humble-rviz_rendering
Requires:       ros2-humble-sensor_msgs
Requires:       ros2-humble-std_msgs
Requires:       ros2-humble-tf2
Requires:       ros2-humble-tf2_geometry_msgs
Requires:       ros2-humble-tf2_ros
Requires:       ros2-humble-tinyxml2_vendor
Requires:       ros2-humble-urdf

Provides:  ros2-humble-rviz_common = 11.2.5-1
Obsoletes: ros2-humble-rviz_common < 11.2.5-1



%description
Common rviz API, used by rviz plugins and applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
Requires:       ros2-humble-ament_cmake-devel
Requires:       yaml-cpp-devel
Requires:       ros2-humble-ament_cmake_cppcheck-devel
Requires:       ros2-humble-ament_cmake_cpplint-devel
Requires:       ros2-humble-ament_cmake_gmock-devel
Requires:       ros2-humble-ament_cmake_gtest-devel
Requires:       ros2-humble-ament_cmake_lint_cmake-devel
Requires:       ros2-humble-ament_cmake_uncrustify-devel
Requires:       ros2-humble-ament_cmake_xmllint-devel
Requires:       ros2-humble-ament_lint_auto-devel
Requires:       ros2-humble-ament_package-devel
Requires:       ros2-humble-geometry_msgs-devel
Requires:       ros2-humble-message_filters-devel
Requires:       ros2-humble-pluginlib-devel
Requires:       ros2-humble-rclcpp-devel
Requires:       ros2-humble-resource_retriever-devel
Requires:       ros2-humble-rviz_ogre_vendor-devel
Requires:       ros2-humble-rviz_rendering-devel
Requires:       ros2-humble-sensor_msgs-devel
Requires:       ros2-humble-std_msgs-devel
Requires:       ros2-humble-tf2-devel
Requires:       ros2-humble-tf2_geometry_msgs-devel
Requires:       ros2-humble-tf2_ros-devel
Requires:       ros2-humble-tinyxml2_vendor-devel
Requires:       ros2-humble-urdf-devel

Provides: ros2-humble-rviz_common-devel = 11.2.5-1
Obsoletes: ros2-humble-rviz_common-devel < 11.2.5-1


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

source %{_libdir}/ros2/setup.bash

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
  --install-base %{buildroot}/%{_libdir}/ros2/ \
  --packages-select rviz_common



# remove wrong buildroot prefixes
find %{buildroot}/%{_libdir}/ros2/ -type f -exec sed -i "s:%{buildroot}::g" {} \;

rm -rf %{buildroot}/%{_libdir}/ros2/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

touch files.list
find %{buildroot}/%{_libdir}/ros2/{bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros2/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
# TODO: is cmake/ necessary? it stems from the yaml vendor
find %{buildroot}/%{_libdir}/ros2/{lib*/pkgconfig,include/,cmake/,rviz_common/include/,share/rviz_common/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list

find . -maxdepth 1 -type f -iname "*readme*" | sed "s:^:%%doc :" >> files.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list



find %{buildroot}/%{_libdir}/ros2/ -name *__rosidl_generator_py.so -type f -exec patchelf --remove-rpath  {} \;
# find %{buildroot}/%{_libdir}/ros2/ -name *__rosidl_generator_py.so -type f -exec patchelf --force-rpath --add-rpath "%{_libdir}/ros2/lib" {} \;

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
* 2023-05-01 Ryan Wüest <ryan.wueest@protonmail.com> - humble.11.2.5-1
- Generate specs for humble
