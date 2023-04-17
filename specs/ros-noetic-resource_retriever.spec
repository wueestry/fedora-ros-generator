Name:           ros-noetic-resource_retriever
Version:        noetic.1.12.7
Release:        1%{?dist}
Summary:        ROS package resource_retriever

License:        BSD
URL:            http://ros.org/wiki/resource_retriever

Source0:        https://github.com/ros-gbp/resource_retriever-release/archive/release/noetic/resource_retriever/1.12.7-1.tar.gz#/ros-noetic-resource_retriever-1.12.7-source0.tar.gz

Patch0: ros-resource_retriever.build-with-cpp17.patch


# common BRs
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gtest-devel
BuildRequires:  log4cxx-devel
BuildRequires:  python3-devel
BuildRequires:  python-unversioned-command

BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gtest-devel
BuildRequires:  libcurl-devel
BuildRequires:  log4cxx-devel
BuildRequires:  tinyxml-devel
BuildRequires:  ros-noetic-catkin-devel
BuildRequires:  ros-noetic-rosconsole-devel
BuildRequires:  ros-noetic-roslib-devel

Requires:       libcurl
Requires:       python3-rospkg
Requires:       ros-noetic-rosconsole
Requires:       ros-noetic-roslib

Provides:  ros-noetic-resource_retriever = 1.12.7-1
Obsoletes: ros-noetic-resource_retriever < 1.12.7-1
Obsoletes: ros-kinetic-resource_retriever < 1.12.7-1



%description
This package retrieves data from url-format files such as http://,
ftp://, package:// file://, etc., and loads the data into memory. The
package:// url for ros packages is translated into a local file://
url. The resourse retriever was initially designed to load mesh files
into memory, but it can be used for any type of data. The resource
retriever is based on the the libcurl library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ros-noetic-catkin-devel
Requires:       boost-devel
Requires:       console-bridge-devel
Requires:       gtest-devel
Requires:       libcurl-devel
Requires:       log4cxx-devel
Requires:       tinyxml-devel
Requires:       ros-noetic-rosconsole-devel
Requires:       ros-noetic-roslib-devel

Provides: ros-noetic-resource_retriever-devel = 1.12.7-1
Obsoletes: ros-noetic-resource_retriever-devel < 1.12.7-1
Obsoletes: ros-kinetic-resource_retriever-devel < 1.12.7-1


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
  --pkg resource_retriever




rm -rf %{buildroot}/%{_libdir}/ros/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh}

touch files.list
find %{buildroot}/%{_libdir}/ros/{bin,etc,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros/{include,lib*/pkgconfig,share/resource_retriever/cmake} \
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
* 2023-04-17 Ryan Wüest <ryan.wueest@protonmail.com> - noetic.1.12.7-1
- Initial desktop generation
