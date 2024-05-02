# Meta Package
Name:           ros-iron-spdlog-vendor
Version:        1.4.4
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/gabime/spdlog
Summary:        Meta package for ros2-iron-spdlog_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-spdlog_vendor
Requires:       ros2-iron-spdlog_vendor-devel

Obsoletes: ros-iron-spdlog-vendor < 1.4.4-1

%description
Wrapper around spdlog, providing nothing but a dependency on spdlog,
on some systems. On others, it provides an ExternalProject build of
spdlog.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.4.4-1
- Update to latest release
