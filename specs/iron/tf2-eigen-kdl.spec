# Meta Package
Name:           ros-iron-tf2-eigen-kdl
Version:        0.31.6
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-tf2_eigen_kdl and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-tf2_eigen_kdl
Requires:       ros2-iron-tf2_eigen_kdl-devel

Obsoletes: ros-iron-tf2-eigen-kdl < 0.31.6-1

%description
Conversion functions between: - Eigen and KDL

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.31.6-1
- Update to latest release
