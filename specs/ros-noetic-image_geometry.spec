Name:           ros-noetic-image_geometry
Version:        noetic.1.16.2
Release:        1%{?dist}
Summary:        ROS package image_geometry

License:        BSD
URL:            http://www.ros.org/

Source0:        https://github.com/ros-gbp/vision_opencv-release/archive/release/noetic/image_geometry/1.16.2-1.tar.gz#/ros-noetic-image_geometry-1.16.2-source0.tar.gz

Patch0: ros-kinetic-image_geometry.catkin-fix-order.patch


# common BRs
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gtest-devel
BuildRequires:  log4cxx-devel
BuildRequires:  python3-devel
BuildRequires:  python-unversioned-command

BuildRequires:  boost-devel
BuildRequires:  gtest-devel
BuildRequires:  opencv-devel
BuildRequires:  ros-noetic-catkin-devel
BuildRequires:  ros-noetic-cpp_common-devel
BuildRequires:  ros-noetic-sensor_msgs-devel


Provides:  ros-noetic-image_geometry = 1.16.2-1
Obsoletes: ros-noetic-image_geometry < 1.16.2-1
Obsoletes: ros-kinetic-image_geometry < 1.16.2-1



%description
`image_geometry` contains C++ and Python libraries for interpreting
images geometrically. It interfaces the calibration parameters in
sensor_msgs/CameraInfo messages with OpenCV functions such as image
rectification, much as cv_bridge interfaces ROS sensor_msgs/Image with
OpenCV data types.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       opencv-devel
Requires:       ros-noetic-catkin-devel
Requires:       ros-noetic-sensor_msgs-devel
Requires:       boost-devel
Requires:       gtest-devel
Requires:       ros-noetic-cpp_common-devel

Provides: ros-noetic-image_geometry-devel = 1.16.2-1
Obsoletes: ros-noetic-image_geometry-devel < 1.16.2-1
Obsoletes: ros-kinetic-image_geometry-devel < 1.16.2-1


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
  --pkg image_geometry




rm -rf %{buildroot}/%{_libdir}/ros/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh}

touch files.list
find %{buildroot}/%{_libdir}/ros/{bin,etc,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros/{include,lib*/pkgconfig,share/image_geometry/cmake} \
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
* 2023-04-17 Ryan Wüest <ryan.wueest@protonmail.com> - noetic.1.16.2-1
- Generate desktop-full
