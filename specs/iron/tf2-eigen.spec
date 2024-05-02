# Meta Package
Name:           ros-iron-tf2-eigen
Version:        0.31.6
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-tf2_eigen and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-tf2_eigen
Requires:       ros2-iron-tf2_eigen-devel

Obsoletes: ros-iron-tf2-eigen < 0.31.6-1

%description
tf2_eigen

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.31.6-1
- Update to latest release
